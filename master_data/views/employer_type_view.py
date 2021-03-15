from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.employer_type_form import EmployerTypeForm
from master_data.models.employer_type import EmployerType
from oagn_covid.settings.base import PAGINATED_BY

class EmployerTypeCreateView(CreateView):
    model = EmployerType
    template_name = "master_data/employer_type/create.html"
    form_class = EmployerTypeForm
    success_url = reverse_lazy('md-employer_type:list')
    
    
class EmployerTypeListView(ListView):
    model = EmployerType
    template_name = "master_data/employer_type/list.html"
    context_object_name = 'employer_types'
    paginate_by = PAGINATED_BY


class EmployerTypeUpdateView(UpdateView):
    model = EmployerType
    template_name = "master_data/employer_type/update.html"
    form_class = EmployerTypeForm
    success_url = reverse_lazy('md-employer_type:list')
    context_object_name = 'employer_type'
    
class EmployerTypeDeleteView(DeleteView):
    model = EmployerType
    template_name = "master_data/employer_type/delete.html"
    success_url = reverse_lazy('md-employer_type:list')
    context_object_name = 'employer_type'
