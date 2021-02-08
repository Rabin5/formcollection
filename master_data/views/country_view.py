from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.country_form import CountryForm
from master_data.models.address import Country
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class CountryCreateView(CreateView):
    model = Country
    template_name = "master_data/address/country_create.html"
    form_class = CountryForm
    success_url = reverse_lazy('md-country:list')


class CountryListView(ListView):
    model = Country
    template_name = "master_data/address/country_list.html"
    context_object_name = 'country_list'
    paginate_by = PAGINATED_BY


class CountryUpdateView(UpdateView):
    model = Country
    template_name = "master_data/address/country_update.html"
    form_class = CountryForm
    success_url = reverse_lazy('md-country:update')
    context_object_name = 'country_update'


class CountryDeleteView(DeleteView):
    model = Country
    template_name = "master_data/address/country_delete.html"
    success_url = reverse_lazy('md-country:list')
    context_object_name = 'country'
