from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.industry_form import IndustryForm
from master_data.models.industry import Industry
from oagn_covid.settings.base import PAGINATED_BY

class IndustryCreateView(CreateView):
    model = Industry
    template_name = "master_data/industry/create.html"
    form_class = IndustryForm
    success_url = reverse_lazy('md-industry:list')
    
    
class IndustryListView(ListView):
    model = Industry
    template_name = "master_data/industry/list.html"
    context_object_name = 'industries'
    paginate_by = PAGINATED_BY


class IndustryUpdateView(UpdateView):
    model = Industry
    template_name = "master_data/industry/update.html"
    form_class = IndustryForm
    success_url = reverse_lazy('md-industry:list')
    context_object_name = 'industry'
    
class IndustryDeleteView(DeleteView):
    model = Industry
    template_name = "master_data/industry/delete.html"
    success_url = reverse_lazy('md-industry:list')
    context_object_name = 'industry'
