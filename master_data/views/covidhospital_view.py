# from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# from master_data.forms.covidhospital_form import CovidHospitalForm
# from master_data.models.company import CovidHospital
# from django.shortcuts import render
# from django.urls import reverse_lazy


# class CovidhospitalCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     model = CovidHospital
#     template_name = "master_data/covidhospital_create.html"
#     form_class = CovidHospitalForm
#     success_url = reverse_lazy('md-covidhospital:list')


# class CovidhospitalListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
#     model = CovidHospital
#     template_name = "master_data/covidhospital_list.html"
#     context_object_name = 'covidhospital_list'


# class CovidhospitalUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
#     model = CovidHospital
#     template_name = "master_data/covidhospital_update.html"
#     form_class = CovidHospitalForm
#     success_url = reverse_lazy('md-covidhospital:update')
#     context_object_name = 'covidhospital_update'
