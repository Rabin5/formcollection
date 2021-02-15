from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.locallevel_form import LocallevelForm
from master_data.models.address import LocalLevel
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class LocalLevelCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = LocalLevel
    template_name = "master_data/address/locallevel_create.html"
    form_class = LocallevelForm
    success_url = reverse_lazy('md-locallevel:list')
    permission_required = 'users.perm_master_data'


class LocalLevelListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = LocalLevel
    template_name = "master_data/address/locallevel_list.html"
    context_object_name = 'locallevel_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class LocalLevelUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = LocalLevel
    template_name = "master_data/address/locallevel_update.html"
    form_class = LocallevelForm
    success_url = reverse_lazy('md-locallevel:list')
    context_object_name = 'locallevel_update'
    permission_required = 'users.perm_master_data'


class LocalLevelDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = LocalLevel
    template_name = "master_data/address/locallevel_delete.html"
    success_url = reverse_lazy('md-locallevel:list')
    context_object_name = 'local'
    permission_required = 'users.perm_master_data'
