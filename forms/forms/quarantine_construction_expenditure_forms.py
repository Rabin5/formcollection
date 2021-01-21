from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.models import QuarantineConstructionExpenditure, QuarantineConstructionExpenditureLine

class QuarantineConstructionExpenditureLineForm(forms.ModelForm):

    class Meta:
        model = QuarantineConstructionExpenditureLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            # if field.widget.input_type != 'select':
            field.widget.attrs['class'] = 'form-control'
            


QuarantineConstructionExpenditureLineFormSet = inlineformset_factory(
    QuarantineConstructionExpenditure, QuarantineConstructionExpenditureLine, form=QuarantineConstructionExpenditureLineForm,
    fields=['quarantine_construction', 'product', 'uom', 'number', 'unit_cost', 'amt_expense', 'procure_method', 'remarks'],
    widgets = {
    },
    extra=1,
    can_delete=False
)


class QuarantineConstructionExpenditureForm(forms.ModelForm):

    class Meta:
        model = QuarantineConstructionExpenditure
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