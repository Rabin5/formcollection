from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from master_data.forms.covidhospital_management_desc_form import CovidHospitalManagementChecklistDescriptionForm
from master_data.models.government import CovidHospitalManagementChecklistDescription
from forms.models.cov_hos_management_checklist import CovidHospitalManagementChecklistLine
from oagn_covid.settings.base import PAGINATED_BY


class CovidHospitalManagementChecklistDescriptionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CovidHospitalManagementChecklistDescription
    template_name = "master_data/cov_hos_managament/cov_hos_managament_create.html"
    form_class = CovidHospitalManagementChecklistDescriptionForm
    success_url = reverse_lazy('md-cov_hos_managament:list')
    permission_required = 'users.perm_master_data'

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.save()
    #     cov_hos = CovidHospitalManagementChecklistLine(description=self.object)
    #     cov_hos.save()

    #     return HttpResponseRedirect(self.success_url)


class CovidHospitalManagementChecklistDescriptionListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CovidHospitalManagementChecklistDescription
    template_name = "master_data/cov_hos_managament/cov_hos_managament_list.html"
    context_object_name = 'cov_hos_managament_typies'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'


class CovidHospitalManagementChecklistDescriptionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CovidHospitalManagementChecklistDescription
    template_name = "master_data/cov_hos_managament/cov_hos_managament_update.html"
    form_class = CovidHospitalManagementChecklistDescriptionForm
    success_url = reverse_lazy('md-cov_hos_managament:list')
    context_object_name = 'cov_hos_managament_type'
    permission_required = 'users.perm_master_data'

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.save()
    #     cov_hos = CovidHospitalManagementChecklistLine(description=self.object)
    #     cov_hos.save()

    #     return HttpResponseRedirect(self.success_url)

class CovidHospitalManagementChecklistDescriptionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CovidHospitalManagementChecklistDescription
    template_name = "master_data/cov_hos_managament/cov_hos_managament_delete.html"
    success_url = reverse_lazy('md-cov_hos_managament:list')
    context_object_name = 'cov_hos_managament_type'
    permission_required = 'users.perm_master_data'
