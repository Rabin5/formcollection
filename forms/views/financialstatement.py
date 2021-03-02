from forms.models.financialstatement import (
    FinancialStatement, FinancialStatementResponsibilityLine,
    FinancialStatementBankAccountReconciledLine, FinancialStatementDeductAmountLine,
    GrantReturnLine, RevenueDistributedLine, RemainingAdvanceLine
)
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from forms.forms.financialstatement import (FinancialStatementResponsibilityLineFormSet, FinancialStatementForm,
                                            FinancialStatementBankAccountReconciledLineFormSet, FinancialStatementDeductAmountLineFormSet, GrantReturnLineFormSet, RevenueDistributedLineFormSet,
                                            RevenueDistributedLineFormSet, FinancialStatementBankAccountReconciledLineForm,
                                            RemainingAdvanceLineFormSet
                                            )


class Financial_St_ResCreateView(CreateView):
    model = FinancialStatement
    template_name = "forms/financialstatement/create.html"
    form_class = FinancialStatementForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = FinancialStatementResponsibilityLineFormSet(
                self.request.POST)
            data['lines1'] = FinancialStatementBankAccountReconciledLineFormSet(
                self.request.POST)
            data['lines2'] = FinancialStatementDeductAmountLineFormSet(
                self.request.POST)
            data['lines3'] = GrantReturnLineFormSet(
                self.request.POST)
            data['lines4'] = RevenueDistributedLineFormSet(
                self.request.POST)
            data['lines5'] = RemainingAdvanceLineFormSet(
                self.request.POST)
        else:
            data['lines'] = FinancialStatementResponsibilityLineFormSet()
            data['lines1'] = FinancialStatementBankAccountReconciledLineFormSet()
            data['lines2'] = FinancialStatementDeductAmountLineFormSet()
            data['lines3'] = GrantReturnLineFormSet()
            data['lines4'] = RevenueDistributedLineFormSet()
            data['lines5'] = RemainingAdvanceLineFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        lines1 = context['lines1']
        lines2 = context['lines2']
        lines3 = context['lines3']
        lines4 = context['lines4']
        lines5 = context['lines5']
        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()
            if lines.is_valid() and lines1.is_valid() and lines2.is_valid() and lines3.is_valid() and lines4.is_valid() and lines5.is_valid():
                lines.instance = self.object
                lines1.instance = self.object
                lines2.instance = self.object
                lines3.instance = self.object
                lines4.instance = self.object
                lines5.instance = self.object
                lines.save()
                lines1.save()
                lines2.save()
                lines3.save()
                lines4.save()
                lines5.save()
        collection = context.get('collection')
        if collection:
            collection.district_covid_management = self.object
            collection.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('finalcial_statement:create')


class Financial_St_ResUpdateView(UpdateView):
    model = FinancialStatement
    template_name = "forms/financialstatement/update.html"
    form_class = FinancialStatementForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(Financial_St_ResUpdateView,
                     self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        if self.request.POST:
            data['lines'] = FinancialStatementResponsibilityLineFormSet(
                self.request.POST, instance=self.object)
            data['lines1'] = FinancialStatementBankAccountReconciledLineFormSet(
                self.request.POST, instance=self.object)
            data['lines2'] = FinancialStatementDeductAmountLineFormSet(
                self.request.POST, instance=self.object)
            data['lines3'] = GrantReturnLineFormSet(
                self.request.POST, instance=self.object)
            data['lines4'] = RevenueDistributedLineFormSet(
                self.request.POST, instance=self.object)
            data['lines5'] = RemainingAdvanceLineFormSet(
                self.request.POST, instance=self.object)

            # data['lines'].full_clean()
        else:
            data['lines'] = FinancialStatementResponsibilityLineFormSet(
                instance=self.object)
            data['lines1'] = FinancialStatementBankAccountReconciledLineFormSet(
                instance=self.object)
            data['lines2'] = FinancialStatementDeductAmountLineFormSet(
                instance=self.object)
            data['lines3'] = GrantReturnLineFormSet(instance=self.object)
            data['lines4'] = RevenueDistributedLineFormSet(
                instance=self.object)
            data['lines5'] = RemainingAdvanceLineFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        lines1 = context['lines1']
        lines2 = context['lines2']
        lines3 = context['lines3']
        lines4 = context['lines4']
        lines5 = context['lines5']

        with transaction.atomic():
            form.instance.create_user = self.request.user
            self.object = form.save()

            if lines.is_valid() and lines1.is_valid() and lines2.is_valid() and lines3.is_valid() and lines4.is_valid() and lines5.is_valid():
                lines.instance = self.object
                lines1.instance = self.object
                lines2.instance = self.object
                lines3.instance = self.object
                lines4.instance = self.object
                lines5.instance = self.object
                lines.save()
                lines1.save()
                lines2.save()
                lines3.save()
                lines4.save()
                lines5.save()
            else:
                return self.form_invalid(form, lines)+self.form_invalid(form, lines1)+self.form_invalid(form, lines2)+self.form_invalid(form, lines3)+self.form_invalid(form, lines4)+self.form_invalid(form, lines5)
        return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(self.get_context_data(form=form, lines=lines)+self.get_context_data(form=form, lines=lines1)+self.get_context_data(form=form, lines=lines2)+self.get_context_data(form=form, lines=lines3)+self.get_context_data(form=form, lines=lines4)+self.get_context_data(form=form, lines=lines5))

    def get_success_url(self):
        return reverse_lazy('finalcial_statement:update', kwargs={'pk': self.object.pk})
