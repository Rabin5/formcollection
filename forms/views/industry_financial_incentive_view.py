from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from forms.models.industry_financial_incentive import IndustryFinancialIncentive
from forms.forms.industry_financial_incentive_forms import IndustryFinancialIncentiveForm, IndustryFinancialIncentiveFormSet


class IndustryFinancialIncentiveCreateView(CreateView):
    model = IndustryFinancialIncentive
    template_name = "forms/industryfinancial_Incentive/create.html"
    form_class = IndustryFinancialIncentiveForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(IndustryFinancialIncentiveCreateView,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = IndustryFinancialIncentiveFormSet(
                self.request.POST)
        else:
            data['lines'] = IndustryFinancialIncentiveFormSet()
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
            collection.isolation_construction_expenditure = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('industry_financial_incentive:create')


class IndustryFinancialIncentiveUpdateView(UpdateView):
    model = IndustryFinancialIncentive
    template_name = "forms/industryfinancial_Incentive/update.html"
    form_class = IndustryFinancialIncentiveForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(IndustryFinancialIncentiveUpdateView,
                     self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = IndustryFinancialIncentiveFormSet(
                self.request.POST, instance=self.object)
            # data['lines'].full_clean()
        else:
            data['lines'] = IndustryFinancialIncentiveFormSet(
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
        return reverse_lazy('industry_financial_incentive:update', kwargs={'pk': self.object.pk})
