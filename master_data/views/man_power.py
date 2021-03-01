from master_data.utils import filter_helper
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.manpower_form import ManpowerForm
from master_data.models.government import Manpower
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class ManpowerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Manpower
    template_name = "master_data/manpower/manpower_create.html"
    form_class = ManpowerForm
    success_url = reverse_lazy('md-manpower:list')
    permission_required = 'users.perm_master_data'


class ManpowerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Manpower
    template_name = "master_data/manpower/manpower_list.html"
    context_object_name = 'manpower_type'
    paginate_by = PAGINATED_BY
    permission_required = 'users.perm_master_data'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        prod = self.model.objects.all()
        # If foreign key then include field__foreignKeyField
        search_list = ['title']
        if query and (len(query) > 2):
            return filter_helper(prod, query, search_list)
        return super().get_queryset()


class ManpowerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Manpower
    template_name = "master_data/manpower/manpower_update.html"
    form_class = ManpowerForm
    success_url = reverse_lazy('md-manpower:list')
    context_object_name = 'manpower_type'
    permission_required = 'users.perm_master_data'


class ManpowerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Manpower
    template_name = "master_data/manpower/manpower_delete.html"
    success_url = reverse_lazy('md-manpower:list')
    context_object_name = 'manpower_type'
    permission_required = 'users.perm_master_data'
