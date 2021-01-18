from django.db import transaction
from django.forms import inlineformset_factory
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import PcrLaboratoryDetail, PcrLaboratoryDetailLine, Laboratory
from forms.forms.pcr_lab_detail_forms import PcrLaboratoryDetailForm, PcrLaboratoryDetailLineFormSet

def get_lab_val(request):
    DATE_CHOICEFIELD = []
    CAPACITY_CHOICEFIELD = []
    lab_value = Laboratory.objects.all().values()
    for lab in lab_value:
        DATE_CHOICEFIELD.append((lab['id'], lab['date_establishment']))
        CAPACITY_CHOICEFIELD.append((lab['id'], lab['capacity_daily_test']))
    
    return JsonResponse({'date_choice': DATE_CHOICEFIELD, 'capacity_choice': CAPACITY_CHOICEFIELD})

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
        # for counter, form in enumerate(lines.forms):
        #     import pdb;pdb.set_trace()
        with transaction.atomic():
            form.instance.create_user = self.request.user
            # self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()
        collection = context.get('collection')
        if collection:
            collection.pcr_lab_detail = self.object
            collection.save()
        
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
        collection = context.get('collection')
        if collection:
            collection.pcr_lab_detail = self.object
            collection.save()
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('pcrlab-forms:update', kwargs={'pk': self.object.pk})
