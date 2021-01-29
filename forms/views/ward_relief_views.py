from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.models.ward_relief_procure_distribution import WardReliefProcureDistribution
from forms.forms.ward_relief_forms import WardReliefProcureDistributionForm, WardReliefProcureDistributionLineForm, WardReliefProcureDistributionFormSet


class WardReliefProcureDistributionCreateView(CreateView):
    model = WardReliefProcureDistribution
    template_name = "forms/ward_relief/create.html"
    form_class = WardReliefProcureDistributionForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = WardReliefProcureDistributionFormSet(
                self.request.POST)
        else:
            data['lines'] = WardReliefProcureDistributionFormSet()
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
        collection = context.get('collection')
        if collection:
            collection.ward_relief_procurement_dist = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ward_relief:ward_relief_create')


class WardReliefProcureDistributionUpdateView(UpdateView):
    model = WardReliefProcureDistribution
    template_name = "forms/ward_relief/update.html"
    form_class = WardReliefProcureDistributionForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = WardReliefProcureDistributionFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = WardReliefProcureDistributionFormSet(
                instance=self.object)
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
            else:
                return self.form_invalid(form, lines)

        return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(self.get_context_data(form=form, lines=lines))

    def get_success_url(self):
        return reverse_lazy('ward_relief:ward_relief_update', kwargs={'pk': self.object.pk})
