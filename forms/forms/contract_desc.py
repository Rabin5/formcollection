from django.db.models import aggregates
from master_data.widgets import NepaliDateInput
from django import forms
from django.forms import widgets
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate, NepaliDateField
from forms.models.contract_desc import ContractDesc, ContractDescLine
from master_data.widgets import NepaliDateInput
import nepali_datetime


class ContractDescLineForm(forms.ModelForm):
    agreement_date = NepaliDateField(label='सम्झौता मिति')

    class Meta:
        model = ContractDescLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            if field.widget.input_type == 'select':
                field.widget.attrs.update({'class': 'select_class'})
            else:
                field.widget.attrs['class'] = 'form-control'


ContractDescFormSet = inlineformset_factory(
    ContractDesc, ContractDescLine, form=ContractDescLineForm,
    fields=['description', 'contractor_name', 'agreement_date',
            'contract_duration', 'contract_amount', 'recover_amount', 'remaining_recover_amount', 'remarks', 'contract_desc'],
    extra=1,
    can_delete=True
)


class ContractDescForm(forms.ModelForm):

    class Meta:
        model = ContractDesc
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
                Fieldset('',
                         Formset('lines')
                         ),

            )
        )
