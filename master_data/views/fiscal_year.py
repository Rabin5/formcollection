from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.fiscal_year import FyForm
from master_data.models import FiscalYear


class FyCreateView(CreateView):
    model = FiscalYear
    template_name = "master_data/fy_create.html"
    form_class = FyForm

    def get_success_url(self):
        return reverse_lazy('md-fy:list')
    # success_url = reverse_lazy('md-fy:list')


class FyListView(ListView):
    model = FiscalYear
    template_name = "master_data/fy_list.html"
    context_object_name = 'fys'


class FyUpdateView(UpdateView):
    model = FiscalYear
    template_name = "master_data/fy_update.html"
    form_class = FyForm
    success_url = reverse_lazy('md-fy:list')
    context_object_name = 'fy'

class FyDeleteView(DeleteView):
    model = FiscalYear
    template_name = "master_data/fy_delete.html"
    success_url = reverse_lazy('md-fy:list')
    context_object_name = 'fy'