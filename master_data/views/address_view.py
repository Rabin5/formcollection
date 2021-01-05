from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.address_form import AddressForm
from master_data.models.company import Address
from django.shortcuts import render
from django.urls import reverse_lazy


class AddressCreateView(CreateView):
    model = Address
    template_name = "master_data/address/address_create.html"
    form_class = AddressForm
    success_url = reverse_lazy('md-address:list')


class AddressListView(ListView):
    model = Address
    template_name = "master_data/address/address_list.html"
    context_object_name = 'address_list'


class AddressUpdateView(UpdateView):
    model = Address
    template_name = "master_data/address/address_update.html"
    form_class = AddressForm
    success_url = reverse_lazy('md-address:update')
    context_object_name = 'address_update'


class AddressDeleteView(DeleteView):
    model = Address
    template_name = "master_data/address/address_delete.html"
    success_url = reverse_lazy('md-address:list')
    context_object_name = 'address'
