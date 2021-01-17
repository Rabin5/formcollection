from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models.rdttestdetail import RdtTestDetailLine, RdtTestDetail


class RdtTestForm(forms.ModelForm):
    class Meta:
        model = RdtTestDetail
        exclude = ()


RdtTestFormSet = inlineformset_factory(
    RdtTestDetail, RdtTestDetailLine, form=RdtTestForm,
    fields=['laboratory', 'num_tested_fy_end', 'num_tested_pcr',
            'expense_rdt_test', ],
    extra=1,
    can_delete=True
)


class RdtTestFormLine(forms.ModelForm):

    class Meta:
        model = RdtTestDetail
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
