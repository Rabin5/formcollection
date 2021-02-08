from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from master_data.forms.committee_form import CommitteeForm
from master_data.models.government import Committee
from oagn_covid.settings.base import PAGINATED_BY


class CommitteeCreateView(CreateView):
    model = Committee
    template_name = "master_data/committee/committee_create.html"
    form_class = CommitteeForm
    success_url = reverse_lazy('md-committee:list')


class CommitteeListView(ListView):
    model = Committee
    template_name = "master_data/committee/committee_list.html"
    context_object_name = 'committee_typies'
    paginate_by = PAGINATED_BY


class CommitteeUpdateView(UpdateView):
    model = Committee
    template_name = "master_data/committee/committee_update.html"
    form_class = CommitteeForm
    success_url = reverse_lazy('md-committee:list')
    context_object_name = 'committee_type'

class CommitteeDeleteView(DeleteView):
    model = Committee
    template_name = "master_data/committee/committee_delete.html"
    success_url = reverse_lazy('md-committee:list')
    context_object_name = 'committee_type'
