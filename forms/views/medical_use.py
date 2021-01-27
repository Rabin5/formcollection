from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from master_data.models.government import GovernmentBody
from forms.models import MedicalUse
from forms.forms.medical_use import MedicalUseLineForm, MedicalUseForm, MedicalUseFormSet


class MedicalUseCreateView(CreateView):
    model = MedicalUse
    template_name = "forms/medical_use/create.html"
    form_class = MedicalUseForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = MedicalUseFormSet(self.request.POST)
        else:
            data['lines'] = MedicalUseFormSet()
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
            collection.medical_use = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('medical-forms:fre-create')


class MedicalUseUpdateView(UpdateView):
    model = MedicalUse
    template_name = "forms/medical_use/update.html"
    form_class = MedicalUseForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = MedicalUseFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = MedicalUseFormSet(instance=self.object)
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
        return reverse_lazy('medical_use:medical_use-update', kwargs={'pk': self.object.pk})
