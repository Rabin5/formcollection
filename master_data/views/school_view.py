from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.school_form import SchoolForm
from master_data.models.school import *
from oagn_covid.settings.base import PAGINATED_BY

class SchoolCreateView(CreateView):
    model = School
    template_name = "master_data/school/school_create.html"
    form_class = SchoolForm
    success_url = reverse_lazy('md-school:list')
    
    
class SchoolListView(ListView):
    model = School
    template_name = "master_data/school/school_list.html"
    context_object_name = 'schools'
    paginate_by = PAGINATED_BY


class SchoolUpdateView(UpdateView):
    model = School
    template_name = "master_data/school/school_update.html"
    form_class = SchoolForm
    success_url = reverse_lazy('md-school:list')
    context_object_name = 'school'
    
class SchoolDeleteView(DeleteView):
    model = School
    template_name = "master_data/school/school_delete.html"
    success_url = reverse_lazy('md-school:list')
    context_object_name = 'school'
