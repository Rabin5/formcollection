from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.convenience_type_form import ConvenienceTypeForm
from master_data.models.convenience_type import *
from oagn_covid.settings.base import PAGINATED_BY

class ConvenienceTypeCreateView(CreateView):
    model = ConvenienceType
    template_name = "master_data/convenience_type/convenience_type_create.html"
    form_class = ConvenienceTypeForm
    success_url = reverse_lazy('md-convenience_type:list')
    
    
class ConvenienceTypeListView(ListView):
    model = ConvenienceType
    template_name = "master_data/convenience_type/convenience_type_list.html"
    context_object_name = 'convenience_types'
    paginate_by = PAGINATED_BY


class ConvenienceTypeUpdateView(UpdateView):
    model = ConvenienceType
    template_name = "master_data/convenience_type/convenience_type_update.html"
    form_class = ConvenienceTypeForm
    success_url = reverse_lazy('md-convenience_type:list')
    context_object_name = 'convenience_type'
    
class ConvenienceTypeDeleteView(DeleteView):
    model = ConvenienceType
    template_name = "master_data/convenience_type/convenience_type_delete.html"
    success_url = reverse_lazy('md-convenience_type:list')
    context_object_name = 'convenience_type'
