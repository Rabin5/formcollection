from django.db import transaction
from django.db.models import query
from django.forms import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls.base import reverse
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

DICT_CH_STATE = {key:value for key, value in CH_STATE}

def query_user_collection(user):
    try:
        val = FormCollection.objects.get(user=user)
        return [val.state, val.get_state_display(), val.get_status_display()]
    except:
        return None

class FormCollectionCreateView(CreateView):
    model = None
    success_url = None
    form_class = ''
    route_link = ''
    form_set = None

    def get_form_class(self):
        self.route_link = ROUTE_LINK.get(self.request.POST.get('current_url').split(":")[0])
        self.form_class = self.route_link[0]
        self.model = self.route_link[2]
        self.form_set = self.route_link[1]
        return self.form_class

    def save_form(self, field_object):
        details = query_user_collection(self.request.user)
        if details is not None:
            if details[0] < len(DICT_CH_STATE):
                print('------------------',DICT_CH_STATE.get(details[0]+1), DICT_CH_STATE.get(details[0]+1)+':create')
                self.success_url = reverse(DICT_CH_STATE.get(details[0]+1)+':create')
                # self.get_success_url(DICT_CH_STATE.get(details[0]+1)+':create')
            

    def form_valid(self, form, model_formset=None):
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if model_formset.is_valid():
                model_formset.instance = self.object
                model_formset.save()
            self.save_form(self.object)
            # print('----------', self.object, dir(self.object), type(self.object))
        print('//////////', HttpResponseRedirect(self.get_success_url()))
        return HttpResponseRedirect(self.get_success_url())
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        model_formset = self.form_set(request.POST)
        if model_formset.is_valid() and form.is_valid():
            return self.form_valid(form, model_formset)
        else:
            return self.form_valid(form)
    
    # def get_success_url(self, url):
    #     return reverse_lazy(url)
    