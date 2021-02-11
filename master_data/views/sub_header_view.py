from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.sub_header_form import SubHeaderForm
from master_data.models.sub_header import *
from oagn_covid.settings.base import PAGINATED_BY

class SubHeaderCreateView(CreateView):
    model = SubHeader
    template_name = "master_data/sub_header/sub_header_create.html"
    form_class = SubHeaderForm
    success_url = reverse_lazy('md-sub_header:list')
    
    
class SubHeaderListView(ListView):
    model = SubHeader
    template_name = "master_data/sub_header/sub_header_list.html"
    context_object_name = 'sub_headers'
    paginate_by = PAGINATED_BY


class SubHeaderUpdateView(UpdateView):
    model = SubHeader
    template_name = "master_data/sub_header/sub_header_update.html"
    form_class = SubHeaderForm
    success_url = reverse_lazy('md-sub_header:list')
    context_object_name = 'sub_header'
    
class SubHeaderDeleteView(DeleteView):
    model = SubHeader
    template_name = "master_data/sub_header/sub_header_delete.html"
    success_url = reverse_lazy('md-sub_header:list')
    context_object_name = 'sub_header'
