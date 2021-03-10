import nepali_datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (ButtonHolder, Column, Div, Fieldset, Hidden,
                                 Layout, Row, Submit)
from django import forms
from django.forms.forms import Form
from django.forms.models import inlineformset_factory
from master_data.widgets import NepaliDateInput

from forms.custom_layout_object import Formset as Formsett
from forms.fields import ModelChoiceFieldWithCreate, NepaliDateField
from forms.models.financialstatement import (
    FinancialStatement, FinancialStatementBankAccountReconciledLine,
    FinancialStatementDeductAmountLine, FinancialStatementResponsibilityLine,
    GrantReturnLine, RemainingAdvanceLine, RevenueDistributedLine)


class FinancialStatementResponsibilityLineForm(forms.ModelForm):
    start_date = NepaliDateField(label='गतको बर्षको अन्तिम मौदात')
    deadline = NepaliDateField(label='यस बर्षको सुरु मौदात')
    # desc = ModelChoiceFieldWithCreate(queryset=FinancialStatementResponsibilityLine.objects.all(
    # ), label='विवरण', blank=False, save_to_field='desc')

    class Meta:
        model = FinancialStatementResponsibilityLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(FinancialStatementResponsibilityLineForm,
              self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            if field.widget.input_type == 'select':
                field.widget.attrs.update({'class': 'select_class'})
            else:
                field.widget.attrs['class'] = 'form-control'
            # to make way of loking field read only
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['way_of_looking'].widget.attrs['readonly'] = True

    def clean_way_of_looking(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.way_of_looking
        else:
            return self.cleaned_data['way_of_looking']


FinancialStatementResponsibilityLineFormSet = inlineformset_factory(
    FinancialStatement, FinancialStatementResponsibilityLine, form=FinancialStatementResponsibilityLineForm,
    fields=['desc', 'is_true', 'deadline', 'start_date',
            'increased_responsibility', 'num_insufficient_bed', 'way_of_looking', 'financialstatement_line'],
    extra=1,
    can_delete=True
)


class FinancialStatementBankAccountReconciledLineForm(forms.ModelForm):
    # desc = ModelChoiceFieldWithCreate(queryset=FinancialStatementBankAccountReconciledLine.objects.all(
    # ), label='विवरण', blank=False, save_to_field='desc')

    class Meta:
        model = FinancialStatementBankAccountReconciledLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(FinancialStatementBankAccountReconciledLineForm,
              self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            if field.widget.input_type == 'select':
                field.widget.attrs.update({'class': 'select_class'})
            else:
                field.widget.attrs['class'] = 'form-control'
            # to make way of loking field read only
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['way_of_looking'].widget.attrs['readonly'] = True

    def clean_way_of_looking(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.way_of_looking
        else:
            return self.cleaned_data['way_of_looking']


FinancialStatementBankAccountReconciledLineFormSet = inlineformset_factory(
    FinancialStatement, FinancialStatementBankAccountReconciledLine, form=FinancialStatementBankAccountReconciledLineForm,
    fields=['desc', 'is_true',
            'remaining_per_account', 'remaining_per_bank', 'difference', 'way_of_looking', 'financialstatement_line'],
    extra=1,
    can_delete=True
)


class FinancialStatementDeductAmountLineForm(forms.ModelForm):
    # desc = ModelChoiceFieldWithCreate(queryset=FinancialStatementDeductAmountLine.objects.all(
    # ), label='विवरण', blank=False, save_to_field='desc')

    class Meta:
        model = FinancialStatementDeductAmountLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(FinancialStatementDeductAmountLineForm,
              self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            if field.widget.input_type == 'select':
                field.widget.attrs.update({'class': 'select_class'})
            else:
                field.widget.attrs['class'] = 'form-control'
        # to make way of loking field read only
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['way_of_looking'].widget.attrs['readonly'] = True

    def clean_way_of_looking(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.way_of_looking
        else:
            return self.cleaned_data['way_of_looking']


FinancialStatementDeductAmountLineFormSet = inlineformset_factory(
    FinancialStatement, FinancialStatementDeductAmountLine, form=FinancialStatementDeductAmountLineForm,
    fields=['desc',  'amount', 'way_of_looking', 'financialstatement_line'
            ],
    extra=1,
    can_delete=True
)


class GrantReturnLineForm(forms.ModelForm):
    # desc = ModelChoiceFieldWithCreate(queryset=GrantReturnLine.objects.all(
    # ), label='विवरण', blank=False, save_to_field='desc')

    class Meta:
        model = GrantReturnLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(GrantReturnLineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            if field.widget.input_type == 'select':
                field.widget.attrs.update({'class': 'select_class'})
            else:
                field.widget.attrs['class'] = 'form-control'
  # to make way of loking field read only
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['way_of_looking'].widget.attrs['readonly'] = True

    def clean_way_of_looking(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.way_of_looking
        else:
            return self.cleaned_data['way_of_looking']


GrantReturnLineFormSet = inlineformset_factory(
    FinancialStatement, GrantReturnLine, form=GrantReturnLineForm,
    fields=['desc', 'is_true', 'remaining_per_federal_government',
            'remaining_per_state_government', 'remaining', 'way_of_looking', 'financialstatement_line'],
    extra=1,
    can_delete=True
)


class RevenueDistributedLineForm(forms.ModelForm):
    # desc = ModelChoiceFieldWithCreate(queryset=RevenueDistributedLine.objects.all(
    # ), label='विवरण', blank=False, save_to_field='desc')

    class Meta:
        model = RevenueDistributedLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(RevenueDistributedLineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            if field.widget.input_type == 'select':
                field.widget.attrs.update({'class': 'select_class'})
            else:
                field.widget.attrs['class'] = 'form-control'

  # to make way of loking field read only
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['way_of_looking'].widget.attrs['readonly'] = True

    def clean_way_of_looking(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.way_of_looking
        else:
            return self.cleaned_data['way_of_looking']


RevenueDistributedLineFormSet = inlineformset_factory(
    FinancialStatement, RevenueDistributedLine, form=RevenueDistributedLineForm,
    fields=['desc', 'is_true', 'remaining_distribution',
            'remaining_amount_federal_gov', 'remaining_amount_state_gov',
            'way_of_looking', 'financialstatement_line'],
    extra=1,
    can_delete=True
)


class RemainingAdvanceLineForm(forms.ModelForm):
    # remaining_advance = ModelChoiceFieldWithCreate(queryset=RemainingAdvanceLine.objects.all(
    # ), label='पेश्की बाँकी', blank=False, save_to_field='desc')

    class Meta:
        model = RemainingAdvanceLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(RemainingAdvanceLineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            if field.widget.input_type == 'select':
                field.widget.attrs.update({'class': 'select_class'})
            else:
                field.widget.attrs['class'] = 'form-control'
    # to make way of loking field read only
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['way_of_looking'].widget.attrs['readonly'] = True

    def clean_way_of_looking(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.way_of_looking
        else:
            return self.cleaned_data['way_of_looking']


RemainingAdvanceLineFormSet = inlineformset_factory(
    FinancialStatement, RemainingAdvanceLine, form=RemainingAdvanceLineForm,
    fields=['remaining_advance',
            'not_expired', 'expired', 'total', 'way_of_looking', 'financialstatement_line'],
    extra=1,
    can_delete=True
)


class FinancialStatementForm(forms.ModelForm):

    class Meta:
        model = FinancialStatement
        fields = '__all__'
        exclude = ('create_user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form_to_submit'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Hidden('next_state', 'next'),
            Row(
                css_class='form-row'
            ),
            Div(

                Fieldset(' जिम्मेवारी फरक परेको',
                         Formsett('lines'), id='1st_fieldest'
                         ),
                Fieldset('बैंक हिसाव मिलान गरेको', Formsett('lines_bankac'),
                         id='2nd_fieldset'),
                Fieldset('कट्टी रकम भुक्तानीरदाखिला गर्न बाकी', Formsett('lines_finalst'),
                         id='3rd_fieldset'),
                Fieldset('अनुदान फिर्ता गर्न बाँकी', Formsett(
                    'lines_grant'), id='4th_fieldset'),
                Fieldset('राजस्व बाँडफाँड रकम पठाउन बाँकी ', Formsett(
                    'lines_renenu'), id='5th_fieldset'),
                Fieldset('पेश्की बाँकी', Formsett('lines_ad'),
                         id='6th_fieldset'),
            )
        )
