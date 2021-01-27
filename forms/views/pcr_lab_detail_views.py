from master_data.models import product
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import PcrLaboratoryDetail, PcrLaboratoryDetailLine, Laboratory
from forms.forms.pcr_lab_detail_forms import PcrLaboratoryDetailForm, PcrLaboratoryDetailLineFormSet
from master_data.forms.laboratory_form import LaboratoryForm

import nepali_datetime
from datetime import datetime

def get_lab_val(request):
    DATE_CHOICEFIELD = {}
    CAPACITY_CHOICEFIELD = {}
    lab_value = Laboratory.objects.all().values('id','capacity_daily_test', 'date_establishment')
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
            data.update(get_lab_val(self.request))
        else:
            data['lines'] = PcrLaboratoryDetailLineFormSet()
            data.update(get_lab_val(self.request))
            
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        
        with transaction.atomic():
            form.instance.create_user = self.request.user
            # self.object = form.save()
            # for line in lines:
            #     print(line['laboratory'])
            #     import pdb;pdb.set_trace()
            # #     print('----------------')
            # #     cont, const = Laboratory.objects.get(line['laboratory'])
            # #     print(cont, const)
            if lines.is_valid():
                for line in lines:
                    data = {
                        'name': line.cleaned_data.get('laboratory'),
                        'capacity_daily_test': line.cleaned_data.get('capacity_daily_test'),
                        'date_establishment': line.cleaned_data.get('date_establishment'),
                    }
                    import pdb;pdb.set_trace()
                    # cont, created = Laboratory.objects.get_or_create(data)
                    # print(cont, created)
                    
                # lines.instance = self.object
                # lines.save()
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
        if self.request.POST:
            data['lines'] = PcrLaboratoryDetailLineFormSet(self.request.POST, instance=self.object)
            data.update(get_lab_val(self.request))
        else:
            data['lines'] = PcrLaboratoryDetailLineFormSet(instance=self.object)
            data.update(get_lab_val(self.request))
        return data
    
    def _process_laboratory(self, line, index):
        """
        Check if laboratory already exists in the database
        if it does, update date establishment and capacity_daily_test values
        If it doesn't, create laboratory with the data from the form
        """
        if line.is_valid():
            laboratory = line.cleaned_data.get('laboratory')
            date_establishment = line.cleaned_data.get('date_establishment')
            capacity_daily_test = line.cleaned_data.get('capacity_daily_test')
            if laboratory and date_establishment and capacity_daily_test:
                date_estd_ad = nepali_datetime.datetime.strptime(date_establishment, '%d/%m/%Y').to_datetime_date()
                Laboratory.objects.filter(pk=laboratory.pk).update(
                    date_establishment=date_estd_ad,
                    capacity_daily_test=capacity_daily_test
                )
        else:
            laboratory = line.data.get(f'lines-{index}-laboratory')
            # Validate if laboratory exists in system already and form is actually invalid
            if laboratory.isnumeric() and \
                Laboratory.objects.filter(pk=int(laboratory)).exists():
                return
            
            capacity = line.cleaned_data.get('capacity_daily_test')
            date_estd = line.cleaned_data.get('date_establishment')
            if laboratory and date_estd and capacity:
                date_estd_ad = nepali_datetime.datetime.strptime(date_estd, '%d/%m/%Y').to_datetime_date()
                data = {'name': laboratory, 'capacity_daily_test': capacity, 'date_establishment':date_estd_ad}
                lab, created = Laboratory.objects.get_or_create(**data)

                line.data._mutable = True  # Update laboratory value in form
                line.data[f'lines-{index}-laboratory'] = f'{lab.id}'
                line.data._mutable = False
                line.cleaned_data.update({'laboratory': lab})
                line.cleaned_data.pop('date_establishment')
                line.cleaned_data.pop('capacity_daily_test')
    
    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            for indx, line in enumerate(lines):
                
                # Process laboratory field
                self._process_laboratory(line, indx)
                    
            lines = context['lines'] = PcrLaboratoryDetailLineFormSet(self.request.POST, instance=self.object)
            if lines.is_valid():
                lines.instance = self.object
                lines.save()
            else:
                return self.form_invalid(form, lines)
        
        return super().form_valid(form)
    
    def form_invalid(self, form, lines=None):
        context=self.get_context_data(form=form, lines=lines)
        return self.render_to_response(context)

    
    def get_success_url(self):
        return reverse_lazy('pcrlab-forms:update', kwargs={'pk': self.object.pk})
