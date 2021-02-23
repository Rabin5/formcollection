from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.contractor_form import ContractorForm
from master_data.models.contractor import *
from oagn_covid.settings.base import PAGINATED_BY

class ContractorCreateView(CreateView):
    model = Contractor
    template_name = "master_data/contractor/contractor_create.html"
    form_class = ContractorForm
    success_url = reverse_lazy('md-contractor:list')
    
    
class ContractorListView(ListView):
    model = Contractor
    template_name = "master_data/contractor/contractor_list.html"
    context_object_name = 'contractors'
    paginate_by = PAGINATED_BY


class ContractorUpdateView(UpdateView):
    model = Contractor
    template_name = "master_data/contractor/contractor_update.html"
    form_class = ContractorForm
    success_url = reverse_lazy('md-contractor:list')
    context_object_name = 'contractor'
    
class ContractorDeleteView(DeleteView):
    model = Contractor
    template_name = "master_data/contractor/contractor_delete.html"
    success_url = reverse_lazy('md-contractor:list')
    context_object_name = 'contractor'
