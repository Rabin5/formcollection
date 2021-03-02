from master_data.utils import filter_helper
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.hospital import CovidHospitalForm, HospitalForm
from master_data.models.hospital import CovidHospital, Hospital
from oagn_covid.settings.base import PAGINATED_BY

class HospitalCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Hospital
    template_name = "master_data/hospital/hos_create.html"
    form_class = HospitalForm
    success_url = reverse_lazy('md-hos:list')
    permission_required = 'users.perm_master_data'


class HospitalListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Hospital
    template_name = "master_data/hospital/hos_list.html"
    context_object_name = 'hospitals'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class HospitalUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Hospital
    template_name = "master_data/hospital/hos_update.html"
    form_class = HospitalForm
    success_url = reverse_lazy('md-hos:list')
    context_object_name = 'hospital'
    permission_required = 'users.perm_master_data'

class HospitalDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Hospital
    template_name = "master_data/hospital/hos_delete.html"
    success_url = reverse_lazy('md-hos:list')
    context_object_name = 'hospital'
    permission_required = 'users.perm_master_data'


class CovidHospitalCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_create.html"
    form_class = CovidHospitalForm
    success_url = reverse_lazy('md-hos:cov_list')
    permission_required = 'users.perm_master_data'


class CovidHospitalListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_list.html"
    context_object_name = 'cov_hospitals'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['type', 'name', 'province__name', 'district__name', 'local_level__name']
        if query and (len(query) > 2):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()


class CovidHospitalUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_update.html"
    form_class = CovidHospitalForm
    success_url = reverse_lazy('md-hos:cov_list')
    context_object_name = 'cov_hospital'
    permission_required = 'users.perm_master_data'

class CovidHospitalDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CovidHospital
    template_name = "master_data/hospital/cov_hos_delete.html"
    success_url = reverse_lazy('md-hos:cov_list')
    context_object_name = 'cov_hospital'
    permission_required = 'users.perm_master_data'