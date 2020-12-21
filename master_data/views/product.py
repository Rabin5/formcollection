from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.product import ProdForm
from master_data.models.product import *


class ProdCreateView(CreateView):
    model = Product
    template_name = "master_data/product/prod_create.html"
    form_class = ProdForm
    success_url = reverse_lazy('md-prod:list')


class ProdListView(ListView):
    model = Product
    template_name = "master_data/product/prod_list.html"
    context_object_name = 'prods'


class ProdUpdateView(UpdateView):
    model = Product
    template_name = "master_data/product/prod_update.html"
    form_class = ProdForm
    success_url = reverse_lazy('md-prod:list')
    context_object_name = 'prod'
