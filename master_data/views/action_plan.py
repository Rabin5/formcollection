from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.action_plan_form import ActionPlanActivityForm
from master_data.models.government import ActionPlanActivity
from oagn_covid.settings.base import PAGINATED_BY

from master_data.utils import *

class ActionPlanActivityCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ActionPlanActivity
    template_name = "master_data/action_plan/action_plan_create.html"
    form_class = ActionPlanActivityForm
    success_url = reverse_lazy('md-action_plan:list')
    permission_required = 'users.perm_master_data'


class ActionPlanActivityListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ActionPlanActivity
    template_name = "master_data/action_plan/action_plan_list.html"
    context_object_name = 'action_plan_typies'
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

class ActionPlanActivityUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ActionPlanActivity
    template_name = "master_data/action_plan/action_plan_update.html"
    form_class = ActionPlanActivityForm
    success_url = reverse_lazy('md-action_plan:list')
    context_object_name = 'action_plan_type'
    permission_required = 'users.perm_master_data'

class ActionPlanActivityDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ActionPlanActivity
    template_name = "master_data/action_plan/action_plan_delete.html"
    success_url = reverse_lazy('md-action_plan:list')
    context_object_name = 'action_plan_type'
    permission_required = 'users.perm_master_data'
