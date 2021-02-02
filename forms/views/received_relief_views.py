from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.models.received_relief_detail import ReceivedReliefDetail
from forms.forms.received_relief_forms import ReceivedReliefDetailForm, ReceivedReliefDetailLineForm, ReceivedReliefDetailFormSet


class ReceivedReliefDetailCreateView(CreateView):
    model = ReceivedReliefDetail
    template_name = "forms/received_relief/create.html"
    form_class = ReceivedReliefDetailForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ReceivedReliefDetailFormSet(
                self.request.POST)
        else:
            data['lines'] = ReceivedReliefDetailFormSet()
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
            collection.received_relief_detail = self.object
            collection.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('received_relief:received_relief_create')


class ReceivedReliefDetailUpdateView(UpdateView):
    model = ReceivedReliefDetail
    template_name = "forms/received_relief/update.html"
    form_class = ReceivedReliefDetailForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = ReceivedReliefDetailFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = ReceivedReliefDetailFormSet(
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
        return reverse_lazy('received_relief:received_relief_update', kwargs={'pk': self.object.pk})
