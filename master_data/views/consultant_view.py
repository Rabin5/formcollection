from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.consultant_form import ConsultantForm
from master_data.models.consultant import *
from oagn_covid.settings.base import PAGINATED_BY

class ConsultantCreateView(CreateView):
    model = Consultant
    template_name = "master_data/consultant/consultant_create.html"
    form_class = ConsultantForm
    success_url = reverse_lazy('md-consultant:list')
    
    
class ConsultantListView(ListView):
    model = Consultant
    template_name = "master_data/consultant/consultant_list.html"
    context_object_name = 'consultants'
    paginate_by = PAGINATED_BY


class ConsultantUpdateView(UpdateView):
    model = Consultant
    template_name = "master_data/consultant/consultant_update.html"
    form_class = ConsultantForm
    success_url = reverse_lazy('md-consultant:list')
    context_object_name = 'consultant'
    
class ConsultantDeleteView(DeleteView):
    model = Consultant
    template_name = "master_data/consultant/consultant_delete.html"
    success_url = reverse_lazy('md-consultant:list')
    context_object_name = 'consultant'
