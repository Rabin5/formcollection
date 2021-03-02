from master_data.utils import filter_helper
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.locallevel_form import LocallevelForm
from master_data.models.address import LocalLevel
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class LocalLevelCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = LocalLevel
    template_name = "master_data/address/locallevel_create.html"
    form_class = LocallevelForm
    success_url = reverse_lazy('md-locallevel:list')
    permission_required = 'users.perm_master_data'


class LocalLevelListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = LocalLevel
    template_name = "master_data/address/locallevel_list.html"
    context_object_name = 'locallevel_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['name', 'district__name', 'district__province__name']
        if query and (len(query) > 2):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()


class LocalLevelUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = LocalLevel
    template_name = "master_data/address/locallevel_update.html"
    form_class = LocallevelForm
    success_url = reverse_lazy('md-locallevel:list')
    context_object_name = 'locallevel_update'
    permission_required = 'users.perm_master_data'


class LocalLevelDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = LocalLevel
    template_name = "master_data/address/locallevel_delete.html"
    success_url = reverse_lazy('md-locallevel:list')
    context_object_name = 'local'
    permission_required = 'users.perm_master_data'
