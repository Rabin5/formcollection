from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import PcrLaboratoryDetail, PcrLaboratoryDetailLine
from forms.forms.pcr_lab_detail_forms import PcrLaboratoryDetailForm, PcrLaboratoryDetailLineFormSet

class PcrLaboratoryDetailCreateView(CreateView):
    model = PcrLaboratoryDetail
    template_name = "forms/pcr_lab_detail/create.html"
    form_class = PcrLaboratoryDetailForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = PcrLaboratoryDetailLineFormSet(self.request.POST)
        else:
            data['lines'] = PcrLaboratoryDetailLineFormSet()
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
        return reverse_lazy('pcrlab-forms:create')


class PcrLaboratoryDetailUpdateView(UpdateView):
    model = PcrLaboratoryDetail
    template_name = "forms/pcr_lab_detail/update.html"
    form_class = PcrLaboratoryDetailForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(PcrLaboratoryDetailUpdateView, self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = PcrLaboratoryDetailLineFormSet(self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = PcrLaboratoryDetailLineFormSet(instance=self.object)
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
        return reverse_lazy('pcrlab-forms:update', kwargs={'pk': self.object.pk})