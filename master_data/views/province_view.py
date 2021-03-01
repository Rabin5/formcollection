from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.province_form import DistrictFormLine, DistrictFormFormSet
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from master_data.models.address import Province
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db import transaction
from oagn_covid.settings.base import PAGINATED_BY

from master_data.utils import filter_helper

class ProvinceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Province
    template_name = "master_data/address/province_create.html"
    form_class = DistrictFormLine
    success_url = reverse_lazy('md-province:list')
    permission_required = 'users.perm_master_data'

    def get_context_data(self, **kwargs):
        data = super(ProvinceCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = DistrictFormFormSet(self.request.POST)
        else:
            data['lines'] = DistrictFormFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('md-province:list')


class ProvinceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Province
    template_name = "master_data/address/province_list.html"
    context_object_name = 'province_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['name']
        if query and (len(query) > 2):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()


class ProvinceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Province
    template_name = "master_data/address/province_update.html"
    form_class = DistrictFormLine
    context_object_name = 'province_update'
    permission_required = 'users.perm_master_data'

    def get_context_data(self, **kwargs):
        data = super(ProvinceUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = DistrictFormFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = DistrictFormFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('md-province:list')


class ProvinceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Province
    template_name = "master_data/address/province_delete.html"
    success_url = reverse_lazy('md-province:list')
    context_object_name = 'province'
    permission_required = 'users.perm_master_data'
