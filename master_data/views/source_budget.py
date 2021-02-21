from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.source_budget_form import SourceBudgetForm
from master_data.models.government import SourceBudget
from oagn_covid.settings.base import PAGINATED_BY


class SourceBudgetCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = SourceBudget
    template_name = "master_data/source_budget/source_budget_create.html"
    permission_required = 'users.perm_master_data'
    form_class = SourceBudgetForm
    success_url = reverse_lazy('md-source_budget:list')


class SourceBudgetListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = SourceBudget
    template_name = "master_data/source_budget/source_budget_list.html"
    context_object_name = 'source_budget_typies'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class SourceBudgetUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = SourceBudget
    template_name = "master_data/source_budget/source_budget_update.html"
    form_class = SourceBudgetForm
    success_url = reverse_lazy('md-source_budget:list')
    context_object_name = 'source_budget_type'
    permission_required = 'users.perm_master_data'

class SourceBudgetDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = SourceBudget
    template_name = "master_data/source_budget/source_budget_delete.html"
    success_url = reverse_lazy('md-source_budget:list')
    context_object_name = 'source_budget_type'
    permission_required = 'users.perm_master_data'
