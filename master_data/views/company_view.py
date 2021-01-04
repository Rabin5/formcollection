from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.company_form import CompanyForm
from master_data.models.company import Company
from django.shortcuts import render
from django.urls import reverse_lazy


class CompanyCreateView(CreateView):
    model = Company
    template_name = "master_data/company/company_create.html"
    form_class = CompanyForm
    success_url = reverse_lazy('md-company:list')


class CompanyListView(ListView):
    model = Company
    template_name = "master_data/company/company_list.html"
    context_object_name = 'company_list'


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = "master_data/company/company_update.html"
    form_class = CompanyForm
    success_url = reverse_lazy('md-company:update')
    context_object_name = 'company_update'


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = "master_data/company/company_delete.html"
    success_url = reverse_lazy('md-company:list')
    context_object_name = 'company'
