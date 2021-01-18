from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models.medical_use import MedicalUseLine, MedicalUse


class MedicalUseForm(forms.ModelForm):

    class Meta:
        model = MedicalUseLine
        exclude = ()


MedicalUseFormSet = inlineformset_factory(
    MedicalUse, MedicalUseLine, form=MedicalUseForm,
    fields=['product', 'is_purchased', 'product_price',
            'unused_qty', 'unused_reason', 'remarks'],
    extra=1,
    can_delete=True
)


class MedicalUseFormLine(forms.ModelForm):

    class Meta:
        model = MedicalUse
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('body'),
                Field('fiscal_year'),
                Fieldset('Add lines. . .',
                         Formset('lines')
                         ),
                HTML('<br>'),
                ButtonHolder(Submit('submit', 'save')),
            )
        )
