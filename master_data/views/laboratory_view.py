from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.laboratory_form import LaboratoryForm
from master_data.models.company import Laboratory
from django.shortcuts import render
from django.urls import reverse_lazy


class LaboratoryCreateView(CreateView):
    model = Laboratory
    template_name = "master_data/laboratory_create.html"
    form_class = LaboratoryForm
    success_url = reverse_lazy('md-laboratory:list')


class LaboratoryListView(ListView):
    model = Laboratory
    template_name = "master_data/laboratory_list.html"
    context_object_name = 'laboratory_list'


class LaboratoryUpdateView(UpdateView):
    model = Laboratory
    template_name = "master_data/laboratory_update.html"
    form_class = LaboratoryForm
    success_url = reverse_lazy('md-laboratory:update')
    context_object_name = 'laboratory_update'
