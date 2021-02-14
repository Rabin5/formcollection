from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.medical_use import MedicalUseLine, MedicalUse, Product


class MedicalUseLineForm(forms.ModelForm):
    product = ModelChoiceFieldWithCreate(queryset=Product.objects.all(), label='औषधी स्वास्थ्य सामग्री एवं उपकरणको नाम', blank=False, save_to_field='name')

    class Meta:
        model = MedicalUseLine
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


MedicalUseFormSet = inlineformset_factory(
    MedicalUse, MedicalUseLine, form=MedicalUseLineForm,
    fields=['product', 'is_purchased', 'product_price',
            'unused_qty', 'unused_reason', 'remarks'],
    extra=1,
    can_delete=True
)


class MedicalUseForm(forms.ModelForm):

    class Meta:
        model = MedicalUse
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
                Fieldset('',
                    Formset('lines')
                ),
            )
        )