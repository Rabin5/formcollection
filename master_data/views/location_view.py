from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.location_form import LocationForm
from master_data.models.company import Location
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class LocationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Location
    template_name = "master_data/company/location_create.html"
    form_class = LocationForm
    permission_required = 'users.perm_master_data'
    success_url = reverse_lazy('md-location:list')


class LocationListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Location
    template_name = "master_data/company/location_list.html"
    context_object_name = 'location_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class LocationUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Location
    template_name = "master_data/company/location_update.html"
    form_class = LocationForm
    success_url = reverse_lazy('md-locallevel:list')
    context_object_name = 'location_update'
    permission_required = 'users.perm_master_data'


class LocationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Location
    template_name = "master_data/company/location_delete.html"
    success_url = reverse_lazy('md-location:list')
    context_object_name = 'location'
    permission_required = 'users.perm_master_data'
