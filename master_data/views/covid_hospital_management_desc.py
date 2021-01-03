from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.covidhospital_management_desc_form import CovidHospitalManagementChecklistDescriptionForm
from master_data.models.government import CovidHospitalManagementChecklistDescription


class CovidHospitalManagementChecklistDescriptionCreateView(CreateView):
    model = CovidHospitalManagementChecklistDescription
    template_name = "master_data/cov_hos_managament/cov_hos_managament_create.html"
    form_class = CovidHospitalManagementChecklistDescriptionForm
    success_url = reverse_lazy('md-cov_hos_managament:list')


class CovidHospitalManagementChecklistDescriptionListView(ListView):
    model = CovidHospitalManagementChecklistDescription
    template_name = "master_data/cov_hos_managament/cov_hos_managament_list.html"
    context_object_name = 'cov_hos_managament_typies'


class CovidHospitalManagementChecklistDescriptionUpdateView(UpdateView):
    model = CovidHospitalManagementChecklistDescription
    template_name = "master_data/cov_hos_managament/cov_hos_managament_update.html"
    form_class = CovidHospitalManagementChecklistDescriptionForm
    success_url = reverse_lazy('md-cov_hos_managament:list')
    context_object_name = 'cov_hos_managament_type'

class CovidHospitalManagementChecklistDescriptionDeleteView(DeleteView):
    model = CovidHospitalManagementChecklistDescription
    template_name = "master_data/cov_hos_managament/cov_hos_managament_delete.html"
    success_url = reverse_lazy('md-cov_hos_managament:list')
    context_object_name = 'cov_hos_managament_type'
