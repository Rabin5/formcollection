from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.designation_form import DesignationForm
from master_data.models.designation import *
from oagn_covid.settings.base import PAGINATED_BY

class DesignationCreateView(CreateView):
    model = Designation
    template_name = "master_data/designation/designation_create.html"
    form_class = DesignationForm
    success_url = reverse_lazy('md-designation:list')
    
    
class DesignationListView(ListView):
    model = Designation
    template_name = "master_data/designation/designation_list.html"
    context_object_name = 'designations'
    paginate_by = PAGINATED_BY


class DesignationUpdateView(UpdateView):
    model = Designation
    template_name = "master_data/designation/designation_update.html"
    form_class = DesignationForm
    success_url = reverse_lazy('md-designation:list')
    context_object_name = 'designation'
    
class DesignationDeleteView(DeleteView):
    model = Designation
    template_name = "master_data/designation/designation_delete.html"
    success_url = reverse_lazy('md-designation:list')
    context_object_name = 'designation'
