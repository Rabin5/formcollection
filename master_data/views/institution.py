from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.institution import InstitutionForm
from master_data.models.company import Institution
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class InstitutionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Institution
    template_name = "master_data/company/institution_create.html"
    form_class = InstitutionForm
    success_url = reverse_lazy('md-institution:list')
    permission_required = 'users.perm_master_data'


class InstitutionListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Institution
    template_name = "master_data/company/institution_list.html"
    context_object_name = 'institution_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class InstitutionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Institution
    template_name = "master_data/company/institution_update.html"
    form_class = InstitutionForm
    success_url = reverse_lazy('md-institution:update')
    context_object_name = 'institution_update'
    permission_required = 'users.perm_master_data'


class InstitutionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Institution
    template_name = "master_data/company/institution_delete.html"
    success_url = reverse_lazy('md-institution:list')
    context_object_name = 'institution'
    permission_required = 'users.perm_master_data'
