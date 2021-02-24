from master_data.utils import filter_helper
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.laboratory_form import LaboratoryForm
from master_data.models.company import Laboratory
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class LaboratoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Laboratory
    template_name = "master_data/company/laboratory_create.html"
    form_class = LaboratoryForm
    success_url = reverse_lazy('md-laboratory:list')
    permission_required = 'users.perm_master_data'


class LaboratoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Laboratory
    template_name = "master_data/company/laboratory_list.html"
    context_object_name = 'laboratory_list'
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


class LaboratoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Laboratory
    template_name = "master_data/company/laboratory_update.html"
    form_class = LaboratoryForm
    success_url = reverse_lazy('md-laboratory:update')
    context_object_name = 'laboratory_update'
    permission_required = 'users.perm_master_data'


class LaboratoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Laboratory
    template_name = "master_data/company/laboratory_delete.html"
    success_url = reverse_lazy('md-laboratory:list')
    context_object_name = 'laboratory'
    permission_required = 'users.perm_master_data'
