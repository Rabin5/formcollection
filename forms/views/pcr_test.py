from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from collection.utils import BS_MONTHS

from forms.models.pcr_test_compliance_detail import PcrTestComplianceDetail
from forms.forms.pcr_test import PcrTestForm, PcrTestFormSet


class PcrTestCreateView(CreateView):
    model = PcrTestComplianceDetail
    template_name = "forms/pcr_test/create.html"
    form_class = PcrTestForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = PcrTestFormSet(self.request.POST)
        else:
            data['lines'] = PcrTestFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()
        collection = context.get('collection')
        if collection:
            collection.pcr_test_compliance_detail = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('pcr_test-forms:create')


class PcrTestUpdateView(UpdateView):
    model = PcrTestComplianceDetail
    template_name = "forms/pcr_test/update.html"
    form_class = PcrTestForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = [
            {
                'month': BS_MONTHS[11][0],
                'year': 2076
            },
            {
                'month': BS_MONTHS[0][0],
                'year': 2077
            },
            {
                'month': BS_MONTHS[1][0],
                'year': 2077
            },
            {
                'month': BS_MONTHS[2][0],
                'year': 2077
            }
        ]
        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = PcrTestFormSet(
                self.request.POST,
                instance=self.object,
                initial=initial
            )
        else:
            data['lines'] = PcrTestFormSet(
                instance=self.object,
                initial=initial
            )
            data['lines'].extra = len(initial) if initial else 1
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()
            else:
                return self.form_invalid(form, lines)

        return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(
            self.get_context_data(form=form, lines=lines)
        )

    def get_success_url(self):
        return reverse_lazy(
            'pcr_test-forms:update',
            kwargs={'pk': self.object.pk}
        )
