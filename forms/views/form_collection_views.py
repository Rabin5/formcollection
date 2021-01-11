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
from forms.models import FormCollection, risk_allowance
from django.apps import apps

from .save_data import save_model
from forms.utils import CH_STATE

from forms.forms.riskallowance_forms import RiskAllowanceForm, RiskAllowanceLineFormSet
from forms.forms.med_exp_forms import MedExpForm, MedExpLineFormSet
from forms.forms.form_collection_forms import FormCollectionForm
from forms.models import MedicalExpense, RiskAllowance


# Asign form, model, form collection field to route view name
ROUTE_LINK = {
    'risk_forms': [RiskAllowanceForm, RiskAllowanceLineFormSet, RiskAllowance, 'risk_allowance'],
    'med_forms': [MedExpForm, MedExpLineFormSet, MedicalExpense, 'med_exp'],
}

# Convert utils CH_STATE to dict
DICT_CH_STATE = {key:value for key, value in CH_STATE}


def query_user_collection(user, pk=None):
    '''
        This function return necessary field of form collection 

        Parameters:
            user(str): Current logged in user
            pk(int): Id of current form updated

        Returns:
            list: Necessary field values
    '''
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
    field_form = None

    def get_form_class(self):
        '''
            Set CreateView attributes. Assigning desired model, form set, form class, form collection field to insert

            Parameters:
                None
            
            Returns:
                form_class(Form): Model formset to be inserted
        '''
        self.route_link = ROUTE_LINK.get(self.request.POST.get('current_url').split(":")[0])
        self.form_class = self.route_link[0]
        self.model = self.route_link[2]
        self.form_set = self.route_link[1]
        self.field_form = self.route_link[3]
        return self.form_class

    def save_form(self, field_object):
        '''
            Stores instance of form model to form collection field and return next url

            Parameters:
                field_object(dict): Form collection {field: objectInstance}

            Returns:
                None
        '''
        form_obj = FormCollection(**field_object)
        # form_obj = FormCollectionForm(field_object)
        form_obj.save()
        # import pdb;pdb.set_trace()
        details = query_user_collection(self.request.user)
        if details is not None:
            if details[0] < len(DICT_CH_STATE):
                self.success_url = reverse(DICT_CH_STATE.get(details[0]+1)+':create')
        else:
            self.success_url = reverse(self.request.POST.get('current_url'))
            

    def form_valid(self, form, model_formset=None):
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if model_formset.is_valid():
                model_formset.instance = self.object
                model_formset.save()
                self.save_form({self.field_form:self.object})
        # return HttpResponseRedirect(self.success_url)
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        model_formset = self.form_set(request.POST)
        if model_formset.is_valid() and form.is_valid():
            return self.form_valid(form, model_formset)
        else:
            return self.form_valid(form)
    
    # def get_success_url(self, url):
    #     return reverse_lazy(url)
    