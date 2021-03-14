from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView
from forms.forms.case_investigation_tracing_forms import CaseInvestigationTracingForm,CaseInvestigationLineForm,CaseInvestigationTracingFormSet
from forms.models.case_investigation_tracing import CaseInvestigationTracing


class CaseInvestigationTracingCreateView(CreateView):
    model = CaseInvestigationTracing
    template_name = 'forms/case_investigation_tracing/create.html'
    form_class =CaseInvestigationTracingForm
    success_url = None

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] =CaseInvestigationTracingFormSet(self.request.POST)
        else:
            data['lines'] = CaseInvestigationTracingFormSet()
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
            collection.case_investigation_tracing = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('case_investigation_forms:conditional-grant-create')


class CaseInvestigationTracingUpdateView(UpdateView):
    model = CaseInvestigationTracing
    template_name = 'forms/case_investigation_tracing/update.html'
    form_class = CaseInvestigationTracingForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(CaseInvestigationTracingUpdateView,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = CaseInvestigationTracingFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = CaseInvestigationTracingFormSet(instance=self.object)
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
        return self.render_to_response(self.get_context_data(form=form, lines=lines))

    def get_success_url(self):
        return reverse_lazy('case_investigation_forms:conditional-grant-update', kwargs={'pk': self.object.pk})
