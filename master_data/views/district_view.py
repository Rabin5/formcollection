from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.district_form import DistrictForm
from master_data.models.address import District
from django.shortcuts import render
from django.urls import reverse_lazy


class DistrictCreateView(CreateView):
    model = District
    template_name = "master_data/address/district_create.html"
    form_class = DistrictForm
    success_url = reverse_lazy('md-district:list')


class DistrictListView(ListView):
    model = District
    template_name = "master_data/address/district_list.html"
    context_object_name = 'district_list'


class DistrictUpdateView(UpdateView):
    model = District
    template_name = "master_data/address/district_update.html"
    form_class = DistrictForm
    success_url = reverse_lazy('md-province:update')
    context_object_name = 'district_update'
