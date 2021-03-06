from master_data.utils import filter_helper
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.quaranrine_form import QuanrantineCenterForm
from master_data.models.company import QuanrantineCenter
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class QuanrantineCenterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = QuanrantineCenter
    template_name = "master_data/company/quarantine_create.html"
    form_class = QuanrantineCenterForm
    success_url = reverse_lazy('md-quarantine:list')
    permission_required = 'users.perm_master_data'


class QuanrantineCenterListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = QuanrantineCenter
    template_name = "master_data/company/quarantine_list.html"
    context_object_name = 'quarantine_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['name', 'province__name', 'district__name', 'local_level__name']
        if query and (len(query) > 2):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()


class QuanrantineCenterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = QuanrantineCenter
    template_name = "master_data/company/quarantine_update.html"
    form_class = QuanrantineCenterForm
    success_url = reverse_lazy('md-quarantine:list')
    context_object_name = 'quarantine'
    permission_required = 'users.perm_master_data'


class QuanrantineCenterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = QuanrantineCenter
    template_name = "master_data/company/quarantine_delete.html"
    success_url = reverse_lazy('md-quarantine:list')
    context_object_name = 'quarantine'
    permission_required = 'users.perm_master_data'
