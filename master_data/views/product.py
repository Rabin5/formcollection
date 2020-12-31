from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.product import ProdForm, UomForm
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

class UomCreateView(CreateView):
    model = UnitOfMeasure
    template_name = "master_data/uom/uom_create.html"
    form_class = UomForm
    success_url = reverse_lazy('md-prod:uom_list')


class UomListView(ListView):
    model = UnitOfMeasure
    template_name = "master_data/uom/uom_list.html"
    context_object_name = 'uoms'


class UomUpdateView(UpdateView):
    model = UnitOfMeasure
    template_name = "master_data/uom/uom_update.html"
    form_class = UomForm
    success_url = reverse_lazy('md-prod:uom_list')
    context_object_name = 'uom'