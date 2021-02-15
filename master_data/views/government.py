from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.government import GovernmentBodyForm, GovernmentBodyTypeForm
from master_data.models.government import GovernmentBody, GovernmentBodyType
from oagn_covid.settings.base import PAGINATED_BY

class GovernmentBodyTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = GovernmentBodyType
    template_name = "master_data/gov_body/gov_body_type_create.html"
    form_class = GovernmentBodyTypeForm
    success_url = reverse_lazy('md-gov:gov_type_list')
    permission_required = 'users.perm_master_data'


class GovernmentBodyTypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = GovernmentBodyType
    template_name = "master_data/gov_body/gov_body_type_list.html"
    context_object_name = 'gov_body_typies'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class GovernmentBodyTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = GovernmentBodyType
    template_name = "master_data/gov_body/gov_body_type_update.html"
    form_class = GovernmentBodyTypeForm
    success_url = reverse_lazy('md-gov:gov_type_list')
    context_object_name = 'gov_body_type'
    permission_required = 'users.perm_master_data'

class GovernmentBodyTypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = GovernmentBodyType
    template_name = "master_data/gov_body/gov_body_type_delete.html"
    success_url = reverse_lazy('md-gov:gov_type_list')
    context_object_name = 'gov_body_type'
    permission_required = 'users.perm_master_data'

class GovernmentBodyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = GovernmentBody
    template_name = "master_data/gov_body/gov_body_create.html"
    form_class = GovernmentBodyForm
    success_url = reverse_lazy('md-gov:list')
    permission_required = 'users.perm_master_data'


class GovernmentBodyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = GovernmentBody
    template_name = "master_data/gov_body/gov_body_list.html"
    context_object_name = 'gov_bodies'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class GovernmentBodyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = GovernmentBody
    template_name = "master_data/gov_body/gov_body_update.html"
    form_class = GovernmentBodyForm
    success_url = reverse_lazy('md-gov:list')
    context_object_name = 'gov_body'
    permission_required = 'users.perm_master_data'

class GovernmentBodyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = GovernmentBody
    template_name = "master_data/gov_body/gov_body_delete.html"
    success_url = reverse_lazy('md-gov:list')
    context_object_name = 'gov_body'
    permission_required = 'users.perm_master_data'