from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from master_data.models.government import GovernmentBody
from forms.models import EmploymentAssessment
from forms.forms.employment_assessment_forms import EmploymentAssessmentForm, EmploymentAssessmentFormSet


class EmploymentAssessmentCreateView(CreateView):
    model = EmploymentAssessment
    template_name = "forms/employment_assessment/create.html"
    form_class = EmploymentAssessmentForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = EmploymentAssessmentFormSet(self.request.POST)
        else:
            data['lines'] = EmploymentAssessmentFormSet()
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
            collection.employment_assessment = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employment_assessment-forms:create')


class EmploymentAssessmentUpdateView(UpdateView):
    model = EmploymentAssessment
    template_name = "forms/employment_assessment/update.html"
    form_class = EmploymentAssessmentForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = EmploymentAssessmentFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = EmploymentAssessmentFormSet(instance=self.object)
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
        return reverse_lazy('employment_assessment-forms:update', kwargs={'pk': self.object.pk})
