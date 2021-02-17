from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.work_nature_form import WorkNatureForm
from master_data.models.work_nature import *
from oagn_covid.settings.base import PAGINATED_BY

class WorkNatureCreateView(CreateView):
    model = WorkNature
    template_name = "master_data/work_nature/work_nature_create.html"
    form_class = WorkNatureForm
    success_url = reverse_lazy('md-work_nature:list')
    
    
class WorkNatureListView(ListView):
    model = WorkNature
    template_name = "master_data/work_nature/work_nature_list.html"
    context_object_name = 'work_natures'
    paginate_by = PAGINATED_BY


class WorkNatureUpdateView(UpdateView):
    model = WorkNature
    template_name = "master_data/work_nature/work_nature_update.html"
    form_class = WorkNatureForm
    success_url = reverse_lazy('md-work_nature:list')
    context_object_name = 'work_nature'
    
class WorkNatureDeleteView(DeleteView):
    model = WorkNature
    template_name = "master_data/work_nature/work_nature_delete.html"
    success_url = reverse_lazy('md-work_nature:list')
    context_object_name = 'work_nature'
