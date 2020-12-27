from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.institution import InstitutionForm
from master_data.models.company import Institution
from django.shortcuts import render
from django.urls import reverse_lazy


class InstitutionCreateView(CreateView):
    model = Institution
    template_name = "master_data/institution_create.html"
    form_class = InstitutionForm
    success_url = reverse_lazy('md-institution:list')


class InstitutionListView(ListView):
    model = Institution
    template_name = "master_data/institution_list.html"
    context_object_name = 'institution_list'


class InstitutionUpdateView(UpdateView):
    model = Institution
    template_name = "master_data/institution_update.html"
    form_class = InstitutionForm
    success_url = reverse_lazy('md-institution:update')
    context_object_name = 'institution_update'
