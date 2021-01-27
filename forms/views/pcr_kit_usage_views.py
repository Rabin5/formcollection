from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models import PcrKitUsage, PcrKitUsageLine
from forms.forms.pcr_kit_usage_forms import PcrKitUsageForm, PcrKitUsageLineFormSet


class PcrKitUsageCreateView(CreateView):
    model = PcrKitUsage
    template_name = "forms/pcr_kit_usage/create.html"
    form_class = PcrKitUsageForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = PcrKitUsageLineFormSet(self.request.POST)
        else:
            data['lines'] = PcrKitUsageLineFormSet()
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
            collection.pcr_kit_usage = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('pcrKit-forms:create')


class PcrKitUsageUpdateView(UpdateView):
    model = PcrKitUsage
    template_name = "forms/pcr_kit_usage/update.html"
    form_class = PcrKitUsageForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(PcrKitUsageUpdateView, self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = PcrKitUsageLineFormSet(
                self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = PcrKitUsageLineFormSet(instance=self.object)
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
        return reverse_lazy('pcrKit-forms:update', kwargs={'pk': self.object.pk})
