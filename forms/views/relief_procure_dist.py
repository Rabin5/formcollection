from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.reliefprocuredistribution import ReliefProcureDistribution, ReliefProcureDistributionLine
from forms.forms.relief_procure_dist import ReliefProcureDistributionLineForm, ReliefProcureDistributionFormSet


class ReliefProcureDistributionCreateView(CreateView):
    model = ReliefProcureDistributionLine
    template_name = "forms/relief_procure_dist/create.html"
    form_class = ReliefProcureDistributionLineForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ReliefProcureDistributionFormSet(self.request.POST)
        else:
            data['lines'] = ReliefProcureDistributionFormSet()
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
            collection.risk_allowance = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('relief_procure_dis:create')


class ReliefProcureDistributionUpdateView(UpdateView):
    model = ReliefProcureDistribution
    template_name = "forms/relief_procure_dist/update.html"
    form_class = ReliefProcureDistributionLineForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ReliefProcureDistributionFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = ReliefProcureDistributionFormSet(
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
        return reverse_lazy('relief_procure_dis:update', kwargs={'pk': self.object.pk})
