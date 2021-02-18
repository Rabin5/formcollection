from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.grant_type_form import GrantTypeForm
from master_data.models.grant_type import *
from oagn_covid.settings.base import PAGINATED_BY

class GrantTypeCreateView(CreateView):
    model = GrantType
    template_name = "master_data/grant_type/grant_type_create.html"
    form_class = GrantTypeForm
    success_url = reverse_lazy('md-grant_type:list')
    
    
class GrantTypeListView(ListView):
    model = GrantType
    template_name = "master_data/grant_type/grant_type_list.html"
    context_object_name = 'grant_types'
    paginate_by = PAGINATED_BY


class GrantTypeUpdateView(UpdateView):
    model = GrantType
    template_name = "master_data/grant_type/grant_type_update.html"
    form_class = GrantTypeForm
    success_url = reverse_lazy('md-grant_type:list')
    context_object_name = 'grant_type'
    
class GrantTypeDeleteView(DeleteView):
    model = GrantType
    template_name = "master_data/grant_type/grant_type_delete.html"
    success_url = reverse_lazy('md-grant_type:list')
    context_object_name = 'grant_type'
