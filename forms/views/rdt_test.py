from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.models.rdttestdetail import RdtTestDetail
from forms.forms.rdt_test import RdtTestForm, RdtTestFormSet


class RdtTestCreateView(CreateView):
    model = RdtTestDetail
    template_name = "forms/rdt_test/create.html"
    form_class = RdtTestForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = RdtTestFormSet(self.request.POST)
        else:
            data['lines'] = RdtTestFormSet()
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
        return reverse_lazy('rdt_test-forms:create')


class RdtTestUpdateView(UpdateView):
    model = RdtTestDetail
    template_name = "forms/rdt_test/update.html"
    form_class = RdtTestForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = RdtTestFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = RdtTestFormSet(instance=self.object)
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
        return reverse_lazy('rdt_test-forms:update', kwargs={'pk': self.object.pk})
