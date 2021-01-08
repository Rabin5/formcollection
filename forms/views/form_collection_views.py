from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views import View
from forms import models
from forms.models import FormCollection
from django.apps import apps

from .save_data import save_model
from forms.utils import CH_STATE


# from forms.forms import riskallowance_forms, med_exp_forms 
from forms.forms.riskallowance_forms import RiskAllowanceForm, RiskAllowanceLineFormSet
from forms.forms.med_exp_forms import MedExpForm, MedExpLineFormSet
from forms.models import MedicalExpense, RiskAllowance


# class FormCollectionView(View):
#     def get(self, request, *args, **kwargs):
#         pass

#     def post(self, request, *args, **kwargs):
#         save_model(request)
#         return None

ROUTE_LINK = {
    'risk_forms': [RiskAllowanceForm, RiskAllowanceLineFormSet, RiskAllowance],
    'med_forms': [MedExpForm, MedExpLineFormSet, MedicalExpense],
}

class FormCollectionCreateView(CreateView):
    model = None
    success_url = None
    form_class = ''
    route_link = ''
    form_set = None

    def get_form_class(self):
        # import pdb;pdb.set_trace()
        self.route_link = ROUTE_LINK.get(self.request.POST.get('current_url').split(":")[0])
        self.form_class = self.route_link[0]
        self.model = self.route_link[2]
        self.form_set = self.route_link[1]
        return self.form_class

    # def get_context_data(self, **kwargs):
    #     # import pdb;pdb.set_trace()
    #     data = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['lines'] = self.form_set(self.request.POST)
    #     else:
    #         data['lines'] = self.form_set()
    #     return data

    def form_valid(self, form, model_formset=None):
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if model_formset.is_valid():
                model_formset.instance = self.object
                model_formset.save()
            print('----------', self.object, dir(self.object), type(self.object))
        return super().form_valid(model_formset)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        model_formset = self.form_set(request.POST)
        if model_formset.is_valid() and form.is_valid():
            return self.form_valid(form, model_formset)
        else:
            return self.form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('med_forms:med_exp-create')
        

'''
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
        return reverse_lazy('med_forms:med_exp-create')


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
        return reverse_lazy('med_forms:med_exp-update', kwargs={'pk': self.object.pk})

'''