from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.models.pcr_test_compliance_detail import PcrTestComplianceDetail
from forms.forms.pcr_test import PcrTestFormLine, PcrTestForm, PcrTestFormSet


class PcrTestCreateView(CreateView):
    model = PcrTestComplianceDetail
    template_name = "forms/pcr_test/create.html"
    form_class = PcrTestFormLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = PcrTestFormSet(self.request.POST)
        else:
            data['lines'] = PcrTestFormSet()
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
        return reverse_lazy('medical-forms:fre-create')


class PcrTestUpdateView(UpdateView):
    model = PcrTestComplianceDetail
    template_name = "forms/pcr_test/update.html"
    form_class = PcrTestFormLine
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = PcrTestFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = PcrTestFormSet(instance=self.object)
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
        return reverse_lazy('medical_use:medical_use-update', kwargs={'pk': self.object.pk})
