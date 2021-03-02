from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.models import IntegralAdvancement
from forms.forms.integral_advancement import IntegralAdvancementForm, IntegralAdvancementFormSet


class IntegralAdvancementCreateView(CreateView):
    model = IntegralAdvancement
    template_name = "forms/integral_advancement/create.html"
    form_class = IntegralAdvancementForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = IntegralAdvancementFormSet(self.request.POST)
        else:
            data['lines'] = IntegralAdvancementFormSet()
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

        # collection = context.get('collection')
        # if collection:
        #     collection.integral_advancement = self.object
        #     collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('integral_advancement-forms:create')


class IntegralAdvancementUpdateView(UpdateView):
    model = IntegralAdvancement
    template_name = "forms/integral_advancement/update.html"
    form_class = IntegralAdvancementForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = IntegralAdvancementFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = IntegralAdvancementFormSet(instance=self.object)
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
        return reverse_lazy('integral_advancement-forms:update', kwargs={'pk': self.object.pk})
