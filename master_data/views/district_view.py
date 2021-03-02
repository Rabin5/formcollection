from master_data.utils import filter_helper
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.district_form import LocalLevelForm, LocalLevelFormSet, LocalLevelLine
from master_data.models.address import District
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db import transaction
from oagn_covid.settings.base import PAGINATED_BY


class DistrictCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = District
    template_name = "master_data/address/district_create.html"
    form_class = LocalLevelLine
    success_url = None
    permission_required = 'users.perm_master_data'

    def get_context_data(self, **kwargs):
        data = super(DistrictCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = LocalLevelFormSet(self.request.POST)
        else:
            data['lines'] = LocalLevelFormSet()
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
        return reverse_lazy('md-district:list')


class DistrictListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = District
    template_name = "master_data/address/district_list.html"
    context_object_name = 'district_list'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['name', 'province__name']
        if query and (len(query) != 0):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()


class DistrictUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = District
    template_name = "master_data/address/district_update.html"
    form_class = LocalLevelLine
    success_url = None
    context_object_name = 'district_update'
    permission_required = 'users.perm_master_data'

    def get_context_data(self, **kwargs):
        data = super(DistrictUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            data['lines'] = LocalLevelFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = LocalLevelFormSet(instance=self.object)
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
            else:
                return self.form_invalid(form, lines)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('md-district:list')


class DistrictDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = District
    template_name = 'master_data/address/district_delete.html'
    success_url = reverse_lazy('md-district:list')
    context_object_name = 'district'
    permission_required = 'users.perm_master_data'
