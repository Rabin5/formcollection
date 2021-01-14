from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from master_data.forms.district_form import LocalLevelForm, LocalLevelFormSet, LocalLevelLine
from master_data.models.address import District
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db import transaction


class DistrictCreateView(CreateView):
    model = District
    template_name = "master_data/address/district_create.html"
    form_class = LocalLevelLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(DistrictCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = LocalLevelFormSet(self.request.POST)
        else:
            data['lines'] = LocalLevelFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('md-district:list')


class DistrictListView(ListView):
    model = District
    template_name = "master_data/address/district_list.html"
    context_object_name = 'district_list'


class DistrictUpdateView(UpdateView):
    model = District
    template_name = "master_data/address/district_update.html"
    form_class = LocalLevelLine
    success_url = None
    context_object_name = 'district_update'

    def get_context_data(self, **kwargs):
        data = super(DistrictUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            data['lines'] = LocalLevelFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = LocalLevelFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('md-district:List', kwargs={'pk': self.object.pk})


class DistrictDeleteView(DeleteView):
    model = District
    template_name = 'master_data/address/district_delete.html'
    success_url = reverse_lazy('md-district:list')
    context_object_name = 'district'
