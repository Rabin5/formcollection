from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.hospital import HospitalForm, CovidHospitalForm
from master_data.models.hospital import Hospital, CovidHospital


class HospitalCreateView(CreateView):
    model = Hospital
    template_name = "master_data/hospital/hos_create.html"
    form_class = HospitalForm
    success_url = reverse_lazy('md-hos:list')


class HospitalListView(ListView):
    model = Hospital
    template_name = "master_data/hospital/hos_list.html"
    context_object_name = 'hospitals'


class HospitalUpdateView(UpdateView):
    model = Hospital
    template_name = "master_data/hospital/hos_update.html"
    form_class = HospitalForm
    success_url = reverse_lazy('md-hos:list')
    context_object_name = 'hospital'

class CovidHospitalCreateView(CreateView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_create.html"
    form_class = CovidHospitalForm
    success_url = reverse_lazy('md-hos:cov_list')


class CovidHospitalListView(ListView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_list.html"
    context_object_name = 'cov_hospitals'


class CovidHospitalUpdateView(UpdateView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_update.html"
    form_class = CovidHospitalForm
    success_url = reverse_lazy('md-hos:cov_list')
    context_object_name = 'cov_hospital'