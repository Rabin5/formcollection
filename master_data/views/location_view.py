from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.location_form import LocationForm
from master_data.models.company import Location
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class LocationCreateView(CreateView):
    model = Location
    template_name = "master_data/company/location_create.html"
    form_class = LocationForm
    success_url = reverse_lazy('md-location:list')


class LocationListView(ListView):
    model = Location
    template_name = "master_data/company/location_list.html"
    context_object_name = 'location_list'
    paginate_by = PAGINATED_BY


class LocationUpdateView(UpdateView):
    model = Location
    template_name = "master_data/company/location_update.html"
    form_class = LocationForm
    success_url = reverse_lazy('md-locallevel:list')
    context_object_name = 'location_update'


class LocationDeleteView(DeleteView):
    model = Location
    template_name = "master_data/company/location_delete.html"
    success_url = reverse_lazy('md-location:list')
    context_object_name = 'location'
