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
            data['lines_bankac'] = FinancialStatementBankAccountReconciledLineFormSet(
                self.request.POST)
            data['lines_finalst'] = FinancialStatementDeductAmountLineFormSet(
                self.request.POST)
            data['lines_grant'] = GrantReturnLineFormSet(
                self.request.POST)
            data['lines_renenu'] = RevenueDistributedLineFormSet(
                self.request.POST)
            data['lines_ad'] = RemainingAdvanceLineFormSet(
                self.request.POST)
        else:
            data['lines'] = FinancialStatementResponsibilityLineFormSet()
            data['lines_bankac'] = FinancialStatementBankAccountReconciledLineFormSet()
            data['lines_finalst'] = FinancialStatementDeductAmountLineFormSet()
            data['lines_grant'] = GrantReturnLineFormSet()
            data['lines_renenu'] = RevenueDistributedLineFormSet()
            data['lines_ad'] = RemainingAdvanceLineFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        lines1 = context['lines_bankac']
        lines2 = context['lines_finalst']
        lines3 = context['lines_grant']
        lines4 = context['lines_renenu']
        lines5 = context['lines_ad']
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

    def _get_initial_data(self):
        if self.object.lines.all():
            return None

        initial = [
            {
                'desc': 'जिम्मेवारी फरक परेको',
                'way_of_looking': 'प्राप्ती र भुक्तानी हिसाबको च र गत बर्षको मौदात भिडाउने',

            },
        ]
        return initial

    def _get_initial_data1(self):
        if self.object.lines_bankac.all():
            return None
        initial1 = [
            {
                'desc': 'बैंक हिसाव मिलान गरेको',
                'way_of_looking': 'प्राप्ती र भुक्तानी हिसाबको (ङ + च) रकम र अनुसूची २४ अनुसूची २४ मा बैंक फरक रकम देखाएको भए सो समेत बुझ्ने',
            },
        ]
        return initial1

    def _get_initial_data2(self):
        if self.object.lines_finalst.all():
            return None
        initial2 = [
            {
                'desc': 'कट्टी रकम भुक्तानीरदाखिला गर्न बाकी',
                'way_of_looking': 'प्राप्ती र भुक्तानी हिसाबको अन्य भुक्तानी घ अन्तर्गत यस्तो रकम राखेको हुनसक्ने',
            },
        ]
        return initial2

    def _get_initial_data3(self):
        if self.object.lines_grant.all():
            return None
        initial3 = [
            {
                'desc': 'अनुदान फिर्ता गर्न बाँकी',
                'way_of_looking': 'सुत्रको वित्तीय विवरणको अनुसूची २१',
            },
        ]
        return initial3

    def _get_initial_data4(self):
        if self.object.lines_renenu.all():
            return None
        initial4 = [
            {
                'desc': 'राजस्व बाँडफाँड रकम पठाउन बाँकी',
                'way_of_looking': 'सुत्रको वित्तीय विवरणको अनुसूची २१',
            },
        ]
        return initial4

    def _get_initial_data5(self):
        if self.object.lines_ad.all():
            return None
        initial5 = [
            {
                'remaining_advance': 'कर्मचारी',
                'way_of_looking': 'सुत्रको वित्तीय विवरणको अनुसूची २३',
            },
            {
                'remaining_advance': 'संस्थागत',
                'way_of_looking': 'सुत्रको वित्तीय विवरणको अनुसूची २३',
            },
            {
                'remaining_advance': 'व्यक्तिगत',
                'way_of_looking': 'सुत्रको वित्तीय विवरणको अनुसूची २३',
            },
        ]
        return initial5

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        initial = self._get_initial_data()
        initial1 = self._get_initial_data1()
        initial2 = self._get_initial_data2()
        initial3 = self._get_initial_data3()
        initial4 = self._get_initial_data4()
        initial5 = self._get_initial_data5()
        print(initial, initial1, initial4)
        if self.request.POST:
            data['lines'] = FinancialStatementResponsibilityLineFormSet(
                self.request.POST, initial=initial)
            data['lines_bankac'] = FinancialStatementBankAccountReconciledLineFormSet(
                self.request.POST, initial=initial1)
            data['lines_finalst'] = FinancialStatementDeductAmountLineFormSet(
                self.request.POST, initial=initial2)
            data['lines_grant'] = GrantReturnLineFormSet(
                self.request.POST, initial=initial3)
            data['lines_renenu'] = RevenueDistributedLineFormSet(
                self.request.POST, initial=initial4)
            data['lines_ad'] = RemainingAdvanceLineFormSet(
                self.request.POST, initial=initial5)
        else:
            data['lines'] = FinancialStatementResponsibilityLineFormSet(
                instance=self.object, initial=initial)
            data['lines_bankac'] = FinancialStatementBankAccountReconciledLineFormSet(
                instance=self.object, initial=initial1)
            data['lines_finalst'] = FinancialStatementDeductAmountLineFormSet(
                instance=self.object, initial=initial2)
            data['lines_grant'] = GrantReturnLineFormSet(
                instance=self.object, initial=initial3)
            data['lines_renenu'] = RevenueDistributedLineFormSet(
                instance=self.object, initial=initial4)
            data['lines_ad'] = RemainingAdvanceLineFormSet(
                instance=self.object, initial=initial5)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        lines1 = context['lines_bankac']
        lines2 = context['lines_finalst']
        lines3 = context['lines_grant']
        lines4 = context['lines_renenu']
        lines5 = context['lines_ad']
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
                return self.form_invalid(form, lines)
        return super().form_valid(form)

    def form_invalid(self, form, lines=None):
        return self.render_to_response(self.get_context_data(form=form, lines=lines))

    def get_success_url(self):
        return reverse_lazy('finalcial_statement:update', kwargs={'pk': self.object.pk})
