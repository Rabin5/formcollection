from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.allowance_type_form import AllowanceTypeForm
from master_data.models.government import AllowanceType
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class AllowanceTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = AllowanceType
    template_name = "master_data/allonace/allowance_type_create.html"
    form_class = AllowanceTypeForm
    success_url = reverse_lazy('md-allowance_type:list')
    permission_required = 'users.perm_master_data'


class AllowanceTypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = AllowanceType
    template_name = "master_data/allonace/allowance_type_list.html"
    context_object_name = 'allowance_type_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class AllowanceTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = AllowanceType
    template_name = "master_data/allonace/allowance_type_update.html"
    form_class = AllowanceTypeForm
    success_url = reverse_lazy('md-allowance_type:list')
    context_object_name = 'allowance_type'
    permission_required = 'users.perm_master_data'


class AllowanceTypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = AllowanceType
    template_name = "master_data/allonace/allowance_type_delete.html"
    success_url = reverse_lazy('md-allowance_type:list')
    context_object_name = 'allowance_type'
    permission_required = 'users.perm_master_data'
