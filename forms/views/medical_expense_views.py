from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import MedicalExpense, MedicalExpenseLine
from forms.forms.med_exp_forms import MedExpForm, MedExpLineFormSet

class MedExpCreateView(CreateView):
    model = MedicalExpense
    template_name = "forms/medical_expense/create.html"
    form_class = MedExpForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = MedExpLineFormSet(self.request.POST)
        else:
            data['lines'] = MedExpLineFormSet()
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
        return reverse_lazy('med_forms:create')


class MedExpUpdateView(UpdateView):
    model = MedicalExpense
    template_name = "forms/medical_expense/update.html"
    form_class = MedExpForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(MedExpUpdateView, self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = MedExpLineFormSet(self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = MedExpLineFormSet(instance=self.object)
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
        return reverse_lazy('med_forms:update', kwargs={'pk': self.object.pk})