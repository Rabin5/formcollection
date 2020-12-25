from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.hospital import CovidHospitalForm
from master_data.models.hospital import CovidHospital

class CovidHospitalCreateView(CreateView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_create.html"
    form_class = CovidHospitalForm
    success_url = reverse_lazy('md-hos:list')


class CovidHospitalListView(ListView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_list.html"
    context_object_name = 'cov_hospitals'


class CovidHospitalUpdateView(UpdateView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_update.html"
    form_class = CovidHospitalForm
    success_url = reverse_lazy('md-hos:list')
    context_object_name = 'cov_hospital'