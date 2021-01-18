from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.risk_allowance import RiskAllowance, RiskAllowanceLine
from forms.forms.riskallowance_forms import RiskAllowanceForm, RiskAllowanceLine, RiskAllowanceLineFormSet


class RiskAllowanceCreateView(CreateView):
    model = RiskAllowance
    template_name = "forms/risk_allowance/create.html"
    form_class = RiskAllowanceForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = RiskAllowanceLineFormSet(self.request.POST)
        else:
            data['lines'] = RiskAllowanceLineFormSet()
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
        return reverse_lazy('risk_forms:create')


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
            data['lines'] = RiskAllowanceLineFormSet(instance=self.object)
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
        return reverse_lazy('risk_forms:update', kwargs={'pk': self.object.pk})
