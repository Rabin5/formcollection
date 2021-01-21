from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import QuarantineManagementDetail, QuarantineManagementDetailLine
from forms.forms.quarantine_management_detail_forms import QuarantineManagementDetailForm, QuarantineManagementDetailLineFormSet


class QuarantineManagementDetailCreateView(CreateView):
    model = QuarantineManagementDetail
    template_name = "forms/quarantine_management/create.html"
    form_class = QuarantineManagementDetailForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = QuarantineManagementDetailLineFormSet(self.request.POST)
        else:
            data['lines'] = QuarantineManagementDetailLineFormSet()
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
        return reverse_lazy('quarantine_forms:create')


class QuarantineManagementDetailUpdateView(UpdateView):
    model = QuarantineManagementDetail
    template_name = "forms/quarantine_management/update.html"
    form_class = QuarantineManagementDetailForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(QuarantineManagementDetailUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = QuarantineManagementDetailLineFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = QuarantineManagementDetailLineFormSet(instance=self.object)
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
        return reverse_lazy('quarantine_forms:update', kwargs={'pk': self.object.pk})
