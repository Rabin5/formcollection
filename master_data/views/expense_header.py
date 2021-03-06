from master_data.utils import filter_helper
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.expense_header_form import ExpenseHeaderForm
from master_data.models.government import ExpenseHeader
from oagn_covid.settings.base import PAGINATED_BY


class ExpenseHeaderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ExpenseHeader
    template_name = "master_data/expense_header/expense_header_create.html"
    form_class = ExpenseHeaderForm
    success_url = reverse_lazy('md-expense_header:list')
    permission_required = 'users.perm_master_data'


class ExpenseHeaderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ExpenseHeader
    template_name = "master_data/expense_header/expense_header_list.html"
    context_object_name = 'expense_header_typies'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['title']
        if query and (len(query) != 0):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()


class ExpenseHeaderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ExpenseHeader
    template_name = "master_data/expense_header/expense_header_update.html"
    form_class = ExpenseHeaderForm
    success_url = reverse_lazy('md-expense_header:list')
    context_object_name = 'expense_header_type'
    permission_required = 'users.perm_master_data'

class ExpenseHeaderDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ExpenseHeader
    template_name = "master_data/expense_header/expense_header_delete.html"
    success_url = reverse_lazy('md-expense_header:list')
    context_object_name = 'expense_header_type'
    permission_required = 'users.perm_master_data'
