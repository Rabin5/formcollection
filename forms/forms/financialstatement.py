import nepali_datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (ButtonHolder, Column, Div, Fieldset, Hidden,
                                 Layout, Row, Submit)
from django import forms
from django.forms.forms import Form
from django.forms.models import inlineformset_factory
from master_data.widgets import NepaliDateInput
from forms.fields import ModelChoiceFieldWithCreate, NepaliDateField
from forms.custom_layout_object import Formset as Formsett
from forms.models.financialstatement import (
    FinancialStatement, FinancialStatementBankAccountReconciledLine,
    FinancialStatementDeductAmountLine, FinancialStatementResponsibilityLine,
    GrantReturnLine, RemainingAdvanceLine, RevenueDistributedLine)


class FinancialStatementResponsibilityLineForm(forms.ModelForm):
    start_date = NepaliDateField(label='गतको बर्षको अन्तिम मौदात')
    deadline = NepaliDateField(label='यस बर्षको सुरु मौदात')

    class Meta:
        model = FinancialStatementResponsibilityLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


FinancialStatementResponsibilityLineFormSet = inlineformset_factory(
    FinancialStatement, FinancialStatementResponsibilityLine, form=FinancialStatementResponsibilityLineForm,
    fields=['desc', 'is_true', 'deadline', 'start_date',
            'increased_responsibility', 'num_insufficient_bed', 'way_of_looking'],
    extra=1,
    can_delete=True
)


class FinancialStatementBankAccountReconciledLineForm(forms.ModelForm):

    class Meta:
        model = FinancialStatementBankAccountReconciledLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


FinancialStatementBankAccountReconciledLineFormSet = inlineformset_factory(
    FinancialStatement, FinancialStatementBankAccountReconciledLine, form=FinancialStatementBankAccountReconciledLineForm,
    fields=['desc', 'is_true',
            'remaining_per_account', 'remaining_per_bank', 'difference', 'way_of_looking'],
    extra=1,
    can_delete=True
)


class FinancialStatementDeductAmountLineForm(forms.ModelForm):

    class Meta:
        model = FinancialStatementDeductAmountLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


FinancialStatementDeductAmountLineFormSet = inlineformset_factory(
    FinancialStatement, FinancialStatementDeductAmountLine, form=FinancialStatementDeductAmountLineForm,
    fields=['desc',  'amount', 'way_of_looking',
            ],
    extra=1,
    can_delete=True
)


class GrantReturnLineForm(forms.ModelForm):

    class Meta:
        model = GrantReturnLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


GrantReturnLineFormSet = inlineformset_factory(
    FinancialStatement, GrantReturnLine, form=GrantReturnLineForm,
    fields=['desc', 'is_true', 'remaining_per_federal_government',
            'remaining_per_state_government', 'remaining', 'way_of_looking'],
    extra=1,
    can_delete=True
)


class RevenueDistributedLineForm(forms.ModelForm):

    class Meta:
        model = RevenueDistributedLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


RevenueDistributedLineFormSet = inlineformset_factory(
    FinancialStatement, RevenueDistributedLine, form=RevenueDistributedLineForm,
    fields=['desc', 'is_true', 'remaining_distribution',
            'remaining_amount_federal_gov', 'remaining_amount_state_gov',
            'way_of_looking'],
    extra=1,
    can_delete=True
)


class RemainingAdvanceLineForm(forms.ModelForm):

    class Meta:
        model = RemainingAdvanceLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


RemainingAdvanceLineFormSet = inlineformset_factory(
    FinancialStatement, RemainingAdvanceLine, form=RemainingAdvanceLineForm,
    fields=['remaining_advance',
            'not_expired', 'expired', 'total', 'way_of_looking'],
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
                Column('body', css_class='col-md-6 mb-0'),
                Column('fiscal_year', css_class='col-md-6 mb-0'),
                css_class='form-row'
            ),
            Div(

                Fieldset(' जिम्मेवारी फरक परेको',
                         Formsett('lines'), id='1st_fieldest'
                         ),
                Fieldset('बैंक हिसाव मिलान गरेको', Formsett('lines1'),
                         id='2nd_fieldset'),
                Fieldset('कट्टी रकम भुक्तानीरदाखिला गर्न बाकी', Formsett('lines2'),
                         id='3rd_fieldset'),
                Fieldset('अनुदान फिर्ता गर्न बाँकी', Formsett(
                    'lines3'), id='4th_fieldset'),
                Fieldset('राजस्व बाँडफाँड रकम पठाउन बाँकी ', Formsett(
                    'lines4'), id='5th_fieldset'),
                Fieldset('पेश्की बाँकी', Formsett('lines5'),
                         id='6th_fieldset'),
                ButtonHolder(Submit('submit', 'save')),
            )
        )
