from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.fiscal_year import FyForm
from master_data.models import FiscalYear
from oagn_covid.settings.base import PAGINATED_BY


class FyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = FiscalYear
    template_name = "master_data/fy_create.html"
    form_class = FyForm
    permission_required = 'users.perm_master_data'

    def get_success_url(self):
        return reverse_lazy('md-fy:list')
    # success_url = reverse_lazy('md-fy:list')


class FyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = FiscalYear
    template_name = "master_data/fy_list.html"
    context_object_name = 'fys'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class FyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = FiscalYear
    template_name = "master_data/fy_update.html"
    form_class = FyForm
    success_url = reverse_lazy('md-fy:list')
    context_object_name = 'fy'
    permission_required = 'users.perm_master_data'

class FyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = FiscalYear
    template_name = "master_data/fy_delete.html"
    success_url = reverse_lazy('md-fy:list')
    context_object_name = 'fy'
    permission_required = 'users.perm_master_data'