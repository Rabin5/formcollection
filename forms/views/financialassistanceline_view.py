from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.financialassistanceline import FinancialAssistance
from forms.forms.financialassistanceline_forms import FinancialAssistanceForm, FinancialAssistanceFormSet


class FinancialAssistanceCreateView(CreateView):
    model = FinancialAssistance
    template_name = "forms/financial_assistance/create.html"
    form_class = FinancialAssistanceForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(FinancialAssistanceCreateView,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = FinancialAssistanceFormSet(
                self.request.POST)
        else:
            data['lines'] = FinancialAssistanceFormSet()
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
            collection.isolation_construction_expenditure = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('finalcial_assistence_create:create')


class FinancialAssistanceUpdateView(UpdateView):
    model = FinancialAssistance
    template_name = "forms/financial_assistance/update.html"
    form_class = FinancialAssistanceForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(FinancialAssistanceUpdateView,
                     self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = FinancialAssistanceFormSet(
                self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = FinancialAssistanceFormSet(
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
        return reverse_lazy('finalcial_assistence_create:update', kwargs={'pk': self.object.pk})
