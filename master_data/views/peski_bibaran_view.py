from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.peski_bibaran_form import PeskiBibaranForm
from master_data.models.peski_bibaran import *
from oagn_covid.settings.base import PAGINATED_BY

class PeskiBibaranCreateView(CreateView):
    model = PeskiBibaran
    template_name = "master_data/peski_bibaran/peski_bibaran_create.html"
    form_class = PeskiBibaranForm
    success_url = reverse_lazy('md-peski_bibaran:list')
    
    
class PeskiBibaranListView(ListView):
    model = PeskiBibaran
    template_name = "master_data/peski_bibaran/peski_bibaran_list.html"
    context_object_name = 'peski_bibarans'
    paginate_by = PAGINATED_BY


class PeskiBibaranUpdateView(UpdateView):
    model = PeskiBibaran
    template_name = "master_data/peski_bibaran/peski_bibaran_update.html"
    form_class = PeskiBibaranForm
    success_url = reverse_lazy('md-peski_bibaran:list')
    context_object_name = 'peski_bibaran'
    
class PeskiBibaranDeleteView(DeleteView):
    model = PeskiBibaran
    template_name = "master_data/peski_bibaran/peski_bibaran_delete.html"
    success_url = reverse_lazy('md-peski_bibaran:list')
    context_object_name = 'peski_bibaran'
