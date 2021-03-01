from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.importer_form import ImporterForm
from master_data.models.company import Importer
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY

from master_data.utils import filter_helper

class ImporterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Importer
    template_name = "master_data/company/importer_create.html"
    form_class = ImporterForm
    success_url = reverse_lazy('md-importer:list')
    permission_required = 'users.perm_master_data'


class ImporterListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Importer
    template_name = "master_data/company/importer_list.html"
    context_object_name = 'importer_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['name', 'province__name', 'district__name', 'local_level__name']
        if query and (len(query) > 2):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()



class ImporterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Importer
    template_name = "master_data/company/importer_update.html"
    form_class = ImporterForm
    success_url = reverse_lazy('md-importer:list')
    context_object_name = 'importer_update'
    permission_required = 'users.perm_master_data'


class ImporterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Importer
    template_name = "master_data/company/importer_delete.html"
    success_url = reverse_lazy('md-importer:list')
    context_object_name = 'importer'
    permission_required = 'users.perm_master_data'
