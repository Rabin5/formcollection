from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import MedicalPurchaseDescription, MedicalPurchaseDescriptionLine
from forms.forms.med_purchase_desc_forms import MedPurchaseDescForm, MedPurchaseDescLineFormSet

class MedPurchaseDescCreateView(CreateView):
    model = MedicalPurchaseDescription
    template_name = "forms/med_purchase_desc/create.html"
    form_class = MedPurchaseDescForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = MedPurchaseDescLineFormSet(self.request.POST)
        else:
            data['lines'] = MedPurchaseDescLineFormSet()
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
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('medDesc-forms:create')


class MedPurchaseDescUpdateView(UpdateView):
    model = MedicalPurchaseDescription
    template_name = "forms/med_purchase_desc/update.html"
    form_class = MedPurchaseDescForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(MedPurchaseDescUpdateView, self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = MedPurchaseDescLineFormSet(self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = MedPurchaseDescLineFormSet(instance=self.object)
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
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('medDesc-forms:update', kwargs={'pk': self.object.pk})