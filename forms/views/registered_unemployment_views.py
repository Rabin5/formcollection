from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from master_data.models.government import GovernmentBody
from forms.models import RegisteredUnemployment
from forms.forms.registered_unemployment_forms import RegisteredUnemploymentForm, RegisteredUnemploymentFormSet


class RegisteredUnemploymentCreateView(CreateView):
    model = RegisteredUnemployment
    template_name = "forms/registered_unemployment/create.html"
    form_class = RegisteredUnemploymentForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = RegisteredUnemploymentFormSet(self.request.POST)
        else:
            data['lines'] = RegisteredUnemploymentFormSet()
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
            collection.registered_unemployment = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('registered_unemployment-forms:create')


class RegisteredUnemploymentUpdateView(UpdateView):
    model = RegisteredUnemployment
    template_name = "forms/registered_unemployment/update.html"
    form_class = RegisteredUnemploymentForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = RegisteredUnemploymentFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = RegisteredUnemploymentFormSet(instance=self.object)
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
        return reverse_lazy('registered_unemployment-forms:update', kwargs={'pk': self.object.pk})
