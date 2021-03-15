from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from master_data.models.government import GovernmentBody
from forms.models import DetailToEmployer
from forms.forms.detail_to_employer_forms import DetailToEmployerForm, DetailToEmployerFormSet


class DetailToEmployerCreateView(CreateView):
    model = DetailToEmployer
    template_name = "forms/detail_to_employer/create.html"
    form_class = DetailToEmployerForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = DetailToEmployerFormSet(self.request.POST)
        else:
            data['lines'] = DetailToEmployerFormSet()
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
            collection.detail_to_employer = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail_to_employer-forms:create')


class DetailToEmployerUpdateView(UpdateView):
    model = DetailToEmployer
    template_name = "forms/detail_to_employer/update.html"
    form_class = DetailToEmployerForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = DetailToEmployerFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = DetailToEmployerFormSet(instance=self.object)
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
        return reverse_lazy('detail_to_employer-forms:update', kwargs={'pk': self.object.pk})
