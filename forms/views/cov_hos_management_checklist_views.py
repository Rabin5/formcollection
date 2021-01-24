from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views import View
from forms.models import CovidHospitalManagementChecklist, CovidHospitalManagementChecklistLine
from forms.forms.cov_hos_management_checklist_forms import CovidHospitalManagementChecklistForm, CovidHospitalManagementChecklistLineFormSet


class CovidHospitalManagementChecklistCreateView(CreateView):
    model = CovidHospitalManagementChecklist
    template_name = "forms/cov_hos_management/create.html"
    form_class = CovidHospitalManagementChecklistForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = CovidHospitalManagementChecklistLineFormSet(self.request.POST)
        else:
            data['lines'] = CovidHospitalManagementChecklistLineFormSet()
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
            collection.cov_hos_management_checklist = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('covHosManagement-forms:create')


class CovidHospitalManagementChecklistUpdateView(UpdateView):
    model = CovidHospitalManagementChecklist
    template_name = "forms/cov_hos_management/update.html"
    form_class = CovidHospitalManagementChecklistForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(CovidHospitalManagementChecklistUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = CovidHospitalManagementChecklistLineFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = CovidHospitalManagementChecklistLineFormSet(instance=self.object)
        
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            print(self.request.POST)
            # form.instance.create_user = self.request.user
            # self.object = form.save()
            # if lines.is_valid():
            #     lines.instance = self.object
            #     lines.save()
            # else:
            #     return self.form_invalid(form, lines)

        return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(self.get_context_data(form=form, lines=lines))

    def get_success_url(self):
        return reverse_lazy('covHosManagement-forms:update', kwargs={'pk': self.object.pk})

