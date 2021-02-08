from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.institution import InstitutionForm
from master_data.models.company import Institution
from django.shortcuts import render
from django.urls import reverse_lazy
from oagn_covid.settings.base import PAGINATED_BY


class InstitutionCreateView(CreateView):
    model = Institution
    template_name = "master_data/company/institution_create.html"
    form_class = InstitutionForm
    success_url = reverse_lazy('md-institution:list')


class InstitutionListView(ListView):
    model = Institution
    template_name = "master_data/company/institution_list.html"
    context_object_name = 'institution_list'
    paginate_by = PAGINATED_BY


class InstitutionUpdateView(UpdateView):
    model = Institution
    template_name = "master_data/company/institution_update.html"
    form_class = InstitutionForm
    success_url = reverse_lazy('md-institution:update')
    context_object_name = 'institution_update'


class InstitutionDeleteView(DeleteView):
    model = Institution
    template_name = "master_data/company/institution_delete.html"
    success_url = reverse_lazy('md-institution:list')
    context_object_name = 'institution'
