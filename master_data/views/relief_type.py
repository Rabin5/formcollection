from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from master_data.forms.relief_type_form import ReliefTypeForm
from master_data.models.government import ReliefType
from oagn_covid.settings.base import PAGINATED_BY


class ReliefTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ReliefType
    template_name = "master_data/relief_type/relief_type_create.html"
    form_class = ReliefTypeForm
    success_url = reverse_lazy('md-relief_type:list')
    permission_required = 'users.perm_master_data'


class ReliefTypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ReliefType
    template_name = "master_data/relief_type/relief_type_list.html"
    context_object_name = 'relief_typies'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class ReliefTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ReliefType
    template_name = "master_data/relief_type/relief_type_update.html"
    form_class = ReliefTypeForm
    success_url = reverse_lazy('md-relief_type:list')
    context_object_name = 'relief_type'
    permission_required = 'users.perm_master_data'

class ReliefTypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ReliefType
    template_name = "master_data/relief_type/relief_type_delete.html"
    success_url = reverse_lazy('md-relief_type:list')
    context_object_name = 'relief_type'
    permission_required = 'users.perm_master_data'
