from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.province_form import ProvinceForm
from master_data.models.address import Province
from django.shortcuts import render
from django.urls import reverse_lazy


class ProvinceCreateView(CreateView):
    model = Province
    template_name = "master_data/address/province_create.html"
    form_class = ProvinceForm
    success_url = reverse_lazy('md-province:list')


class ProvinceListView(ListView):
    model = Province
    template_name = "master_data/address/province_list.html"
    context_object_name = 'province_list'


class ProvinceUpdateView(UpdateView):
    model = Province
    template_name = "master_data/address/province_update.html"
    form_class = ProvinceForm
    success_url = reverse_lazy('md-province:update')
    context_object_name = 'province_update'
