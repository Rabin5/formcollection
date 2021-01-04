from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.isolation_form import IsolationCenterForm
from master_data.models.company import IsolationCenter
from django.shortcuts import render
from django.urls import reverse_lazy


class IsolationCenterCreateView(CreateView):
    model = IsolationCenter
    template_name = "master_data/company/isolation_create.html"
    form_class = IsolationCenterForm
    success_url = reverse_lazy('md-quarantine:list')


class IsolationCenterListView(ListView):
    model = IsolationCenter
    template_name = "master_data/company/isolation_list.html"
    context_object_name = 'isolation_list'


class IsolationCenterUpdateView(UpdateView):
    model = IsolationCenter
    template_name = "master_data/company/isolation_update.html"
    form_class = IsolationCenterForm
    success_url = reverse_lazy('md-isolation:list')
    context_object_name = 'isolation_update'


class IsolationCenterDeleteView(DeleteView):
    model = IsolationCenter
    template_name = "master_data/company/isolation_delete.html"
    success_url = reverse_lazy('md-isolation:list')
    context_object_name = 'isolation'
