from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.officebearer_form import OfficeBearerForm
from master_data.models.government import OfficeBearer
from oagn_covid.settings.base import PAGINATED_BY


class OfficeBearerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = OfficeBearer
    template_name = "master_data/office_bearer/office_bearer_create.html"
    form_class = OfficeBearerForm
    success_url = reverse_lazy('md-offbearer:list')
    permission_required = 'users.perm_master_data'


class OfficeBearerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = OfficeBearer
    template_name = "master_data/office_bearer/office_bearer_list.html"
    context_object_name = 'office_bearer_typies'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class OfficeBearerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = OfficeBearer
    template_name = "master_data/office_bearer/office_bearer_update.html"
    form_class = OfficeBearerForm
    success_url = reverse_lazy('md-offbearer:list')
    context_object_name = 'office_bearer_type'
    permission_required = 'users.perm_master_data'

class OfficeBearerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = OfficeBearer
    template_name = "master_data/office_bearer/office_bearer_delete.html"
    success_url = reverse_lazy('md-offbearer:list')
    context_object_name = 'office_bearer_type'
    permission_required = 'users.perm_master_data'
