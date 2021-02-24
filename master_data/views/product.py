from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.product import ProdForm, UomForm, ProcurementForm
from master_data.models.product import *
from oagn_covid.settings.base import PAGINATED_BY

from master_data.utils import *

class ProdCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    template_name = "master_data/product/prod_create.html"
    form_class = ProdForm
    success_url = reverse_lazy('md-prod:list')
    permission_required = 'users.perm_master_data'
    
    
class ProdListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = "master_data/product/prod_list.html"
    context_object_name = 'prods'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['name', 'type', 'uom__name']
        if query and (len(query) != 0):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()
    


class ProdUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = "master_data/product/prod_update.html"
    form_class = ProdForm
    success_url = reverse_lazy('md-prod:list')
    context_object_name = 'prod'
    permission_required = 'users.perm_master_data'
    
class ProdDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "master_data/product/prod_delete.html"
    success_url = reverse_lazy('md-prod:list')
    context_object_name = 'prod'
    permission_required = 'users.perm_master_data'

class UomCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = UnitOfMeasure
    template_name = "master_data/uom/uom_create.html"
    form_class = UomForm
    success_url = reverse_lazy('md-prod:uom_list')
    permission_required = 'users.perm_master_data'


class UomListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = UnitOfMeasure
    template_name = "master_data/uom/uom_list.html"
    context_object_name = 'uoms'
    permission_required = 'users.perm_master_data'
    paginate_by = PAGINATED_BY

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['name']
        if query and (len(query) != 0):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()


class UomUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = UnitOfMeasure
    template_name = "master_data/uom/uom_update.html"
    form_class = UomForm
    success_url = reverse_lazy('md-prod:uom_list')
    context_object_name = 'uom'
    permission_required = 'users.perm_master_data'

class UomDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = UnitOfMeasure
    template_name = "master_data/uom/uom_delete.html"
    success_url = reverse_lazy('md-prod:uom_list')
    context_object_name = 'uom'
    permission_required = 'users.perm_master_data'

class ProcurementCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ProcurementMethod
    template_name = "master_data/procurement_method/procurement_create.html"
    form_class = ProcurementForm
    success_url = reverse_lazy('md-prod:procurement_list')
    permission_required = 'users.perm_master_data'


class ProcurementListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ProcurementMethod
    template_name = "master_data/procurement_method/procurement_list.html"
    context_object_name = 'procurements'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['name']
        if query and (len(query) != 0):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()


class ProcurementUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProcurementMethod
    template_name = "master_data/procurement_method/procurement_update.html"
    form_class = ProcurementForm
    success_url = reverse_lazy('md-prod:procurement_list')
    context_object_name = 'procurement'
    permission_required = 'users.perm_master_data'

class ProcurementDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProcurementMethod
    template_name = "master_data/procurement_method/procurement_delete.html"
    success_url = reverse_lazy('md-prod:procurement_list')
    context_object_name = 'procurement'
    permission_required = 'users.perm_master_data'
