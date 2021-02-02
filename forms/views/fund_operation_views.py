from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.models.fund_operation import FundOperation
from forms.forms.fund_operation_forms import FundOperationForm, FundOperationLineForm, FundOperationFormSet


class FundOperationCreateView(CreateView):
    model = FundOperation
    template_name = "forms/fund_operation/create.html"
    form_class = FundOperationForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = FundOperationFormSet(self.request.POST)
        else:
            data['lines'] = FundOperationFormSet()
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
        return reverse_lazy('fund_operation:fund_operation_create')


class FundOperationUpdateView(UpdateView):
    model =FundOperation
    template_name = "forms/fund_operation/update.html"
    form_class = FundOperationForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = FundOperationFormSet(
                self.request.POST, instance=self.object)
        else:
            data['lines'] = FundOperationFormSet(instance=self.object)
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
        return reverse_lazy('fund_operation:fund_operation_update', kwargs={'pk': self.object.pk})
