from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.project_type_form import ProjectTypeForm
from master_data.models.project_type import *
from oagn_covid.settings.base import PAGINATED_BY

class ProjectTypeCreateView(CreateView):
    model = ProjectType
    template_name = "master_data/project_type/project_type_create.html"
    form_class = ProjectTypeForm
    success_url = reverse_lazy('md-project_type:list')
    
    
class ProjectTypeListView(ListView):
    model = ProjectType
    template_name = "master_data/project_type/project_type_list.html"
    context_object_name = 'project_types'
    paginate_by = PAGINATED_BY


class ProjectTypeUpdateView(UpdateView):
    model = ProjectType
    template_name = "master_data/project_type/project_type_update.html"
    form_class = ProjectTypeForm
    success_url = reverse_lazy('md-project_type:list')
    context_object_name = 'project_type'
    
class ProjectTypeDeleteView(DeleteView):
    model = ProjectType
    template_name = "master_data/project_type/project_type_delete.html"
    success_url = reverse_lazy('md-project_type:list')
    context_object_name = 'project_type'
