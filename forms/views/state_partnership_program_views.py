from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.models import StatePartnershipProgram
from forms.forms.state_partnership_program import StatePartnershipProgramForm, StatePartnershipProgramFormSet


class StatePartnershipProgramtCreateView(CreateView):
    model = StatePartnershipProgram
    template_name = "forms/state_partnership_program/create.html"
    form_class = StatePartnershipProgramForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = StatePartnershipProgramFormSet(self.request.POST)
        else:
            data['lines'] = StatePartnershipProgramFormSet()
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
            collection.state_partnership_program = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('state_partnership_program-forms:create')


class StatePartnershipProgramtUpdateView(UpdateView):
    model = StatePartnershipProgram
    template_name = "forms/state_partnership_program/update.html"
    form_class = StatePartnershipProgramForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = StatePartnershipProgramFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = StatePartnershipProgramFormSet(instance=self.object)
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
        return reverse_lazy('state_partnership_program-forms:update', kwargs={'pk': self.object.pk})
