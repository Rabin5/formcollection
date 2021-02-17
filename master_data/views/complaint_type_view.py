from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.complaint_type_form import ComplaintTypeForm
from master_data.models.complaint_type import *
from oagn_covid.settings.base import PAGINATED_BY

class ComplaintTypeCreateView(CreateView):
    model = ComplaintType
    template_name = "master_data/complaint_type/complaint_type_create.html"
    form_class = ComplaintTypeForm
    success_url = reverse_lazy('md-complaint_type:list')
    
    
class ComplaintTypeListView(ListView):
    model = ComplaintType
    template_name = "master_data/complaint_type/complaint_type_list.html"
    context_object_name = 'complaint_types'
    paginate_by = PAGINATED_BY


class ComplaintTypeUpdateView(UpdateView):
    model = ComplaintType
    template_name = "master_data/complaint_type/complaint_type_update.html"
    form_class = ComplaintTypeForm
    success_url = reverse_lazy('md-complaint_type:list')
    context_object_name = 'complaint_type'
    
class ComplaintTypeDeleteView(DeleteView):
    model = ComplaintType
    template_name = "master_data/complaint_type/complaint_type_delete.html"
    success_url = reverse_lazy('md-complaint_type:list')
    context_object_name = 'complaint_type'
