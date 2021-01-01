from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.risk_allowance import RiskAllowance, RiskAllowanceLine
from forms.forms.riskallowance_forms import RiskAllowanceForm, RiskAllowanceLine, RiskAllowanceFormSet


class RiskAllowanceCreateView(CreateView):
    model = RiskAllowance
    template_name = "forms/risk_allowance/create.html"
    form_class = RiskAllowanceForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = RiskAllowanceFormSet(self.request.POST)
        else:
            data['lines'] = RiskAllowanceFormSet()
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
        return reverse_lazy('forms:fre-create')


class RiskAllowanceUpdateView(UpdateView):
    model = RiskAllowance
    template_name = "forms/risk_allowance/update.html"
    form_class = RiskAllowanceForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = RiskAllowanceLineFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = RiskAllowanceFormFormSet(instance=self.object)
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
        return reverse_lazy('forms:risk_allowance-update', kwargs={'pk': self.object.pk})
