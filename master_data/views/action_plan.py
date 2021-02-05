from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.action_plan_form import ActionPlanActivityForm
from master_data.models.government import ActionPlanActivity
from oagn_covid.settings.base import PAGINATED_BY


class ActionPlanActivityCreateView(CreateView):
    model = ActionPlanActivity
    template_name = "master_data/action_plan/action_plan_create.html"
    form_class = ActionPlanActivityForm
    success_url = reverse_lazy('md-action_plan:list')


class ActionPlanActivityListView(ListView):
    model = ActionPlanActivity
    template_name = "master_data/action_plan/action_plan_list.html"
    context_object_name = 'action_plan_typies'
    paginate_by = PAGINATED_BY

class ActionPlanActivityUpdateView(UpdateView):
    model = ActionPlanActivity
    template_name = "master_data/action_plan/action_plan_update.html"
    form_class = ActionPlanActivityForm
    success_url = reverse_lazy('md-action_plan:list')
    context_object_name = 'action_plan_type'

class ActionPlanActivityDeleteView(DeleteView):
    model = ActionPlanActivity
    template_name = "master_data/action_plan/action_plan_delete.html"
    success_url = reverse_lazy('md-action_plan:list')
    context_object_name = 'action_plan_type'
