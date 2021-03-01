from master_data.utils import filter_helper
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

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['name', 'province__name', 'district__name', 'local_level__name']
        if query and (len(query) > 2):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()


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
