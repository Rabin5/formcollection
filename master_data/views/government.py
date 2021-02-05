from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.government import GovernmentBodyForm, GovernmentBodyTypeForm
from master_data.models.government import GovernmentBody, GovernmentBodyType
from oagn_covid.settings.base import PAGINATED_BY

class GovernmentBodyTypeCreateView(CreateView):
    model = GovernmentBodyType
    template_name = "master_data/gov_body/gov_body_type_create.html"
    form_class = GovernmentBodyTypeForm
    success_url = reverse_lazy('md-gov:gov_type_list')


class GovernmentBodyTypeListView(ListView):
    model = GovernmentBodyType
    template_name = "master_data/gov_body/gov_body_type_list.html"
    context_object_name = 'gov_body_typies'
    paginate_by = PAGINATED_BY


class GovernmentBodyTypeUpdateView(UpdateView):
    model = GovernmentBodyType
    template_name = "master_data/gov_body/gov_body_type_update.html"
    form_class = GovernmentBodyTypeForm
    success_url = reverse_lazy('md-gov:gov_type_list')
    context_object_name = 'gov_body_type'

class GovernmentBodyTypeDeleteView(DeleteView):
    model = GovernmentBodyType
    template_name = "master_data/gov_body/gov_body_type_delete.html"
    success_url = reverse_lazy('md-gov:gov_type_list')
    context_object_name = 'gov_body_type'

class GovernmentBodyCreateView(CreateView):
    model = GovernmentBody
    template_name = "master_data/gov_body/gov_body_create.html"
    form_class = GovernmentBodyForm
    success_url = reverse_lazy('md-gov:list')


class GovernmentBodyListView(ListView):
    model = GovernmentBody
    template_name = "master_data/gov_body/gov_body_list.html"
    context_object_name = 'gov_bodies'
    paginate_by = PAGINATED_BY


class GovernmentBodyUpdateView(UpdateView):
    model = GovernmentBody
    template_name = "master_data/gov_body/gov_body_update.html"
    form_class = GovernmentBodyForm
    success_url = reverse_lazy('md-gov:list')
    context_object_name = 'gov_body'

class GovernmentBodyDeleteView(DeleteView):
    model = GovernmentBody
    template_name = "master_data/gov_body/gov_body_delete.html"
    success_url = reverse_lazy('md-gov:list')
    context_object_name = 'gov_body'