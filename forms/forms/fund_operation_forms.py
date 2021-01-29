from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden,Submit, ButtonHolder

from forms.custom_layout_object import Formset
from forms.models import FundOperation, FundOperationLine


class FundOperationLineForm(forms.ModelForm):

    class Meta:
        model = FundOperationLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


FundOperationFormSet = inlineformset_factory(
    FundOperation, FundOperationLine, form=FundOperationLineForm,
    fields=['body', 'amt_received', 'expense_header',
            'amt_expensed'],
    extra=1,
    can_delete=False
)


class FundOperationForm(forms.ModelForm):

    class Meta:
        model = FundOperation
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
