from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.importer_form import ImporterForm
from master_data.models.company import Importer
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class ImporterCreateView(CreateView):
    model = Importer
    template_name = "master_data/company/importer_create.html"
    form_class = ImporterForm
    success_url = reverse_lazy('md-importer:list')


class ImporterListView(ListView):
    model = Importer
    template_name = "master_data/company/importer_list.html"
    context_object_name = 'importer_list'
    paginate_by = PAGINATED_BY


class ImporterUpdateView(UpdateView):
    model = Importer
    template_name = "master_data/company/importer_update.html"
    form_class = ImporterForm
    success_url = reverse_lazy('md-importer:list')
    context_object_name = 'importer_update'


class ImporterDeleteView(DeleteView):
    model = Importer
    template_name = "master_data/company/importer_delete.html"
    success_url = reverse_lazy('md-importer:list')
    context_object_name = 'importer'
