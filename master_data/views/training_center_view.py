from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.training_center_form import TrainingCenterForm
from master_data.models.training_center import TrainingCenter
from oagn_covid.settings.base import PAGINATED_BY

class TrainingCenterCreateView(CreateView):
    model = TrainingCenter
    template_name = "master_data/training_center/create.html"
    form_class = TrainingCenterForm
    success_url = reverse_lazy('md-training_center:list')
    
    
class TrainingCenterListView(ListView):
    model = TrainingCenter
    template_name = "master_data/training_center/list.html"
    context_object_name = 'training_centers'
    paginate_by = PAGINATED_BY


class TrainingCenterUpdateView(UpdateView):
    model = TrainingCenter
    template_name = "master_data/training_center/update.html"
    form_class = TrainingCenterForm
    success_url = reverse_lazy('md-training_center:list')
    context_object_name = 'training_center'
    
class TrainingCenterDeleteView(DeleteView):
    model = TrainingCenter
    template_name = "master_data/training_center/delete.html"
    success_url = reverse_lazy('md-training_center:list')
    context_object_name = 'training_center'
