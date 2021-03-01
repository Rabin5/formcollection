from master_data.utils import filter_helper
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.committee_form import CommitteeForm
from master_data.models.government import Committee
from oagn_covid.settings.base import PAGINATED_BY


class CommitteeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Committee
    template_name = "master_data/committee/committee_create.html"
    form_class = CommitteeForm
    success_url = reverse_lazy('md-committee:list')
    permission_required = 'users.perm_master_data'


class CommitteeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Committee
    template_name = "master_data/committee/committee_list.html"
    context_object_name = 'committee_typies'
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


class CommitteeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Committee
    template_name = "master_data/committee/committee_update.html"
    form_class = CommitteeForm
    success_url = reverse_lazy('md-committee:list')
    context_object_name = 'committee_type'
    permission_required = 'users.perm_master_data'

class CommitteeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Committee
    template_name = "master_data/committee/committee_delete.html"
    success_url = reverse_lazy('md-committee:list')
    context_object_name = 'committee_type'
    permission_required = 'users.perm_master_data'
