from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.hospital import CovidHospitalForm, HospitalForm
from master_data.models.hospital import CovidHospital, Hospital
from oagn_covid.settings.base import PAGINATED_BY

class HospitalCreateView(CreateView):
    model = Hospital
    template_name = "master_data/hospital/hos_create.html"
    form_class = HospitalForm
    success_url = reverse_lazy('md-hos:list')


class HospitalListView(ListView):
    model = Hospital
    template_name = "master_data/hospital/hos_list.html"
    context_object_name = 'hospitals'
    paginate_by = PAGINATED_BY


class HospitalUpdateView(UpdateView):
    model = Hospital
    template_name = "master_data/hospital/hos_update.html"
    form_class = HospitalForm
    success_url = reverse_lazy('md-hos:list')
    context_object_name = 'hospital'

class HospitalDeleteView(DeleteView):
    model = Hospital
    template_name = "master_data/hospital/hos_delete.html"
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
    paginate_by = PAGINATED_BY


class CovidHospitalUpdateView(UpdateView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_update.html"
    form_class = CovidHospitalForm
    success_url = reverse_lazy('md-hos:cov_list')
    context_object_name = 'cov_hospital'

class CovidHospitalDeleteView(DeleteView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_delete.html"
    success_url = reverse_lazy('md-hos:cov_list')
    context_object_name = 'cov_hospital'