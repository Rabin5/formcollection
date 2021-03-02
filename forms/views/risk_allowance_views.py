from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.risk_allowance import (
    RiskAllowance,
    OfficeBearer
)
from forms.forms.riskallowance_forms import (
    RiskAllowanceForm,
    RiskAllowanceLineFormSet
)


class RiskAllowanceCreateView(CreateView):
    model = RiskAllowance
    template_name = "forms/risk_allowance/create.html"
    form_class = RiskAllowanceForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = RiskAllowanceLineFormSet(self.request.POST)
        else:
            data['lines'] = RiskAllowanceLineFormSet()
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
            collection.risk_allowance = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('risk_forms:create')


class RiskAllowanceUpdateView(UpdateView):
    model = RiskAllowance
    template_name = "forms/risk_allowance/update.html"
    form_class = RiskAllowanceForm
    success_url = None

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = []
        bearers = OfficeBearer.objects.all()[:5]

        for bearer in bearers:
            line = {
                'office_bearer': bearer
            }
            initial.append(line)

        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        initial = self._get_initial_data()
        if self.request.POST:
            data['lines'] = RiskAllowanceLineFormSet(
                self.request.POST, instance=self.object,
                initial=initial
                )
        else:
            data['lines'] = RiskAllowanceLineFormSet(
                instance=self.object, initial=initial
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
        return self.render_to_response(self.get_context_data(
            form=form,
            lines=lines
            )
        )

    def get_success_url(self):
        return reverse_lazy('risk_forms:update', kwargs={'pk': self.object.pk})
