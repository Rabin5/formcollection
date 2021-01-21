from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import QuarantineConstructionExpenditure, QuarantineConstructionExpenditureLine
from forms.forms.quarantine_construction_expenditure_forms import QuarantineConstructionExpenditureForm, QuarantineConstructionExpenditureLineFormSet


class QuarantineConstructionExpenditureCreateView(CreateView):
    model = QuarantineConstructionExpenditure
    template_name = "forms/quarantine_construction/create.html"
    form_class = QuarantineConstructionExpenditureForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = QuarantineConstructionExpenditureLineFormSet(self.request.POST)
        else:
            data['lines'] = QuarantineConstructionExpenditureLineFormSet()
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
        return reverse_lazy('quarantine_construct_forms:create')


class QuarantineConstructionExpenditureUpdateView(UpdateView):
    model = QuarantineConstructionExpenditure
    template_name = "forms/quarantine_construction/update.html"
    form_class = QuarantineConstructionExpenditureForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(QuarantineConstructionExpenditureUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = QuarantineConstructionExpenditureLineFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = QuarantineConstructionExpenditureLineFormSet(instance=self.object)
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
        return reverse_lazy('quarantine_construct_forms:update', kwargs={'pk': self.object.pk})
