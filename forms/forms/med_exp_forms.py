from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models import MedicalExpense, MedicalExpenseLine
from master_data.models import Product, Importer, ProcurementMethod
from master_data.widgets import NepaliDateInput

class MedExpLineForm(forms.ModelForm):
    product = ModelChoiceFieldWithCreate(queryset=Product.objects.all(), blank=False, label='स्वास्थ्य सामाग्री उपकरण', save_to_field='name')
    importer = ModelChoiceFieldWithCreate(queryset=Importer.objects.all(), label='आपूर्तिकर्ताको नाम', save_to_field='name')
    procure_method = ModelChoiceFieldWithCreate(queryset=ProcurementMethod.objects.all(), label='खरिद विधि', blank=False, save_to_field='name')

    class Meta:
        model = MedicalExpenseLine
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
            


MedExpLineFormSet = inlineformset_factory(
    MedicalExpense, MedicalExpenseLine, form=MedExpLineForm,
    fields=['medical_expense', 'product', 'importer', 'amt_agreement', 'date_to_import', 'date_imported', 'amt_imported', 'procure_method', 'remarks'],
    widgets = {
        'date_to_import': NepaliDateInput(),
        'date_imported': NepaliDateInput(),
    },
    extra=1,
    can_delete=True
)


class MedExpForm(forms.ModelForm):

    class Meta:
        model = MedicalExpense
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