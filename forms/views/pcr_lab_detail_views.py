from master_data.models import product
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import PcrLaboratoryDetail, PcrLaboratoryDetailLine, Laboratory
from forms.forms.pcr_lab_detail_forms import PcrLaboratoryDetailForm, PcrLaboratoryDetailLineFormSet
from master_data.forms.laboratory_form import LaboratoryForm

import nepali_datetime

def get_lab_val(request):
    DATE_CHOICEFIELD = {}
    CAPACITY_CHOICEFIELD = {}
    lab_value = Laboratory.objects.all().values()
    for lab in lab_value:
        nep_date = nepali_datetime.date.from_datetime_date(lab['date_establishment'])
        DATE_CHOICEFIELD.update({lab['id']: nep_date.strftime("%d/%m/%Y")})
        CAPACITY_CHOICEFIELD.update({lab['id']: lab['capacity_daily_test']})
    
    return {'date_choice': DATE_CHOICEFIELD, 'capacity_choice': CAPACITY_CHOICEFIELD}

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
            data.update(get_lab_val(self.request))
            
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            # for line in lines:
            #     print(line['laboratory'])
            #     print('----------------')
            #     cont, const = Laboratory.objects.get(line['laboratory'])
            #     print(cont, const)
            # import pdb;pdb.set_trace()
            if lines.is_valid():
                for line in lines:
                    data = {
                        'name': line.cleaned_data.get('laboratory'),
                        'capacity_daily_test': line.cleaned_data.get('capacity_daily_test'),
                        'date_establishment': line.cleaned_data.get('date_establishment'),
                    }
                    # import pdb;pdb.set_trace()
                    # cont, created = Laboratory.objects.get_or_create(data)
                    # print(cont, created)
                    
                lines.instance = self.object
                lines.save()
        collection = context.get('collection')
        if collection:
            collection.pcr_lab_detail = self.object
            collection.save()
        
        return super().form_valid(form)
    
    # def get(self, request, *args, **kwargs):
    #     context = get_lab_val(request)
    #     return self.render_to_response(context)
    #     pass

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
            data.update(get_lab_val(self.request))
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
        return reverse_lazy('pcrlab-forms:update', kwargs={'pk': self.object.pk})
