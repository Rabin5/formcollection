from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.relief_type_form import ReliefTypeForm
from master_data.models.government import ReliefType


class ReliefTypeCreateView(CreateView):
    model = ReliefType
    template_name = "master_data/relief_type/relief_type_create.html"
    form_class = ReliefTypeForm
    success_url = reverse_lazy('md-relief_type:list')


class ReliefTypeListView(ListView):
    model = ReliefType
    template_name = "master_data/relief_type/relief_type_list.html"
    context_object_name = 'relief_typies'


class ReliefTypeUpdateView(UpdateView):
    model = ReliefType
    template_name = "master_data/relief_type/relief_type_update.html"
    form_class = ReliefTypeForm
    success_url = reverse_lazy('md-relief_type:list')
    context_object_name = 'relief_type'

class ReliefTypeDeleteView(DeleteView):
    model = ReliefType
    template_name = "master_data/relief_type/relief_type_delete.html"
    success_url = reverse_lazy('md-relief_type:list')
    context_object_name = 'relief_type'
