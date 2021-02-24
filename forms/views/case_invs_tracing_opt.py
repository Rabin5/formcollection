from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.case_inve_trac_operations import (
    CaseInvestigationTracingOperations
)
from forms.forms.case_invs_tracing_opt import (
    CaseInvestigationTracingOptForm,
    CaseInvestigationTracingOptFormSet
)


class CaseInvTacingOptCreateView(CreateView):
    model = CaseInvestigationTracingOperations
    template_name = "forms/case_inc_tracing_opt/create.html"
    form_class = CaseInvestigationTracingOptForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = CaseInvestigationTracingOptFormSet(
                self.request.POST)
        else:
            data['lines'] = CaseInvestigationTracingOptFormSet()
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
            collection.case_investigation_tracing_operation = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('case_inv_tracing_opt:create')


class CaseInvTacingOptUpdateView(UpdateView):
    model = CaseInvestigationTracingOperations
    template_name = "forms/case_inc_tracing_opt/update.html"
    form_class = CaseInvestigationTracingOptForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = CaseInvestigationTracingOptFormSet(
                self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = CaseInvestigationTracingOptFormSet(
                instance=self.object)
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
            'case_inv_tracing_opt:update',
            kwargs={'pk': self.object.pk}
        )
