from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.construction_company_form import ConstructionCompanyForm
from master_data.models.construction_company import *
from oagn_covid.settings.base import PAGINATED_BY

class ConstructionCompanyCreateView(CreateView):
    model = ConstructionCompany
    template_name = "master_data/construction_company/cons_create.html"
    form_class = ConstructionCompanyForm
    success_url = reverse_lazy('md-construction:list')
    
    
class ConstructionCompanyListView(ListView):
    model = ConstructionCompany
    template_name = "master_data/construction_company/cons_list.html"
    context_object_name = 'construction'
    paginate_by = PAGINATED_BY


class ConstructionCompanyUpdateView(UpdateView):
    model = ConstructionCompany
    template_name = "master_data/construction_company/cons_update.html"
    form_class = ConstructionCompanyForm
    success_url = reverse_lazy('md-construction:list')
    context_object_name = 'cons'
    
class ConstructionCompanyDeleteView(DeleteView):
    model = ConstructionCompany
    template_name = "master_data/construction_company/cons_delete.html"
    success_url = reverse_lazy('md-construction:list')
    context_object_name = 'cons'
