from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.isolation_form import IsolationCenterForm
from master_data.models.company import IsolationCenter
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class IsolationCenterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = IsolationCenter
    template_name = "master_data/company/isolation_create.html"
    form_class = IsolationCenterForm
    success_url = reverse_lazy('md-quarantine:list')
    permission_required = 'users.perm_master_data'


class IsolationCenterListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = IsolationCenter
    template_name = "master_data/company/isolation_list.html"
    context_object_name = 'isolation_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class IsolationCenterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = IsolationCenter
    template_name = "master_data/company/isolation_update.html"
    form_class = IsolationCenterForm
    success_url = reverse_lazy('md-isolation:list')
    context_object_name = 'isolation_update'
    permission_required = 'users.perm_master_data'


class IsolationCenterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = IsolationCenter
    template_name = "master_data/company/isolation_delete.html"
    success_url = reverse_lazy('md-isolation:list')
    context_object_name = 'isolation'
    permission_required = 'users.perm_master_data'
