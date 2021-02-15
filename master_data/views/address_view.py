from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.address_form import AddressForm
from master_data.models.company import Address
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class AddressCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Address
    template_name = "master_data/address/address_create.html"
    form_class = AddressForm
    success_url = reverse_lazy('md-address:list')
    permission_required = 'users.perm_master_data'


class AddressListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model=Address
    template_name = "master_data/address/address_list.html"
    context_object_name = 'address_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'



class AddressUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Address
    template_name = "master_data/address/address_update.html"
    form_class = AddressForm
    success_url = reverse_lazy('md-address:update')
    context_object_name = 'address_update'
    permission_required = 'users.perm_master_data'


class AddressDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Address
    template_name = "master_data/address/address_delete.html"
    success_url = reverse_lazy('md-address:list')
    context_object_name = 'address'
    permission_required = 'users.perm_master_data'
