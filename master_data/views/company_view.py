from master_data.utils import date_filter, filter_helper
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.company_form import CompanyForm
from master_data.models.company import Company
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class CompanyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Company
    template_name = "master_data/company/company_create.html"
    form_class = CompanyForm
    success_url = reverse_lazy('md-company:list')
    permission_required = 'users.perm_master_data'


class CompanyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Company
    template_name = "master_data/company/company_list.html"
    context_object_name = 'company_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)
        prod = self.model.objects.filter()
        # If foreign key then include field__foreignKeyField
        search_list = ['name']

        if start_date:
            prod = date_filter(Company, 'date_establishment')(self.request.GET, queryset=prod).qs.distinct()

        if end_date:
            prod = date_filter(Company, 'date_establishment')(self.request.GET, queryset=prod).qs.distinct()

        if query and (len(query) != 0):
            prod = filter_helper(prod, query, search_list)
        try:
            return prod
        except:
            return super().get_queryset()


class CompanyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Company
    template_name = "master_data/company/company_update.html"
    form_class = CompanyForm
    success_url = reverse_lazy('md-company:update')
    context_object_name = 'company_update'
    permission_required = 'users.perm_master_data'


class CompanyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Company
    template_name = "master_data/company/company_delete.html"
    success_url = reverse_lazy('md-company:list')
    context_object_name = 'company'
    permission_required = 'users.perm_master_data'
