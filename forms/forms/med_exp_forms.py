from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models import MedicalExpense, MedicalExpenseLine
from master_data.widgets import NepaliDateInput

class MedExpLineForm(forms.ModelForm):

    class Meta:
        model = MedicalExpenseLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if field.widget.input_type != 'select':
                field.widget.attrs['class'] = 'form-control'
            


MedExpLineFormSet = inlineformset_factory(
    MedicalExpense, MedicalExpenseLine, form=MedExpLineForm,
    fields=['medical_expense', 'product', 'amt_agreement', 'date_to_import', 'date_imported', 'amt_imported', 'remarks'],
    widgets = {
        'date_to_import': NepaliDateInput(),
        'date_imported': NepaliDateInput(),
    },
    extra=1,
    can_delete=False
)


class MedExpForm(forms.ModelForm):

    class Meta:
        model = MedicalExpense
        fields = '__all__'
        exclude = ('create_user', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Fieldset('',
                    Formset('lines')
                ),
            )
        )