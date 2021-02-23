from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.vehicle_form import VehicleForm
from master_data.models.vehicle import *
from oagn_covid.settings.base import PAGINATED_BY

class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = "master_data/vehicle/vehicle_create.html"
    form_class = VehicleForm
    success_url = reverse_lazy('md-vehicle:list')
    
    
class VehicleListView(ListView):
    model = Vehicle
    template_name = "master_data/vehicle/vehicle_list.html"
    context_object_name = 'vehicles'
    paginate_by = PAGINATED_BY


class VehicleUpdateView(UpdateView):
    model = Vehicle
    template_name = "master_data/vehicle/vehicle_update.html"
    form_class = VehicleForm
    success_url = reverse_lazy('md-vehicle:list')
    context_object_name = 'vehicle'
    
class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = "master_data/vehicle/vehicle_delete.html"
    success_url = reverse_lazy('md-vehicle:list')
    context_object_name = 'vehicle'
