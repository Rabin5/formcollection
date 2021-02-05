from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.expense_header_form import ExpenseHeaderForm
from master_data.models.government import ExpenseHeader
from oagn_covid.settings.base import PAGINATED_BY


class ExpenseHeaderCreateView(CreateView):
    model = ExpenseHeader
    template_name = "master_data/expense_header/expense_header_create.html"
    form_class = ExpenseHeaderForm
    success_url = reverse_lazy('md-expense_header:list')


class ExpenseHeaderListView(ListView):
    model = ExpenseHeader
    template_name = "master_data/expense_header/expense_header_list.html"
    context_object_name = 'expense_header_typies'
    paginate_by = PAGINATED_BY


class ExpenseHeaderUpdateView(UpdateView):
    model = ExpenseHeader
    template_name = "master_data/expense_header/expense_header_update.html"
    form_class = ExpenseHeaderForm
    success_url = reverse_lazy('md-expense_header:list')
    context_object_name = 'expense_header_type'

class ExpenseHeaderDeleteView(DeleteView):
    model = ExpenseHeader
    template_name = "master_data/expense_header/expense_header_delete.html"
    success_url = reverse_lazy('md-expense_header:list')
    context_object_name = 'expense_header_type'
