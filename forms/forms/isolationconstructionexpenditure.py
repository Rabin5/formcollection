from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Div, Fieldset, Hidden, ButtonHolder, Submit, Layout, Row
from django import forms
from django.forms.models import inlineformset_factory

from forms.custom_layout_object import Formset
from forms.models import IsolationConstructionExependiture, IsolationConstructionExependitureLine


class IsolationConstructionExependitureLineForm(forms.ModelForm):

    class Meta:
        model = IsolationConstructionExependitureLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


IsolationConstructionExependitureFormSet = inlineformset_factory(
    IsolationConstructionExependiture, IsolationConstructionExependitureLine, form=IsolationConstructionExependitureLineForm,
    fields=['product', 'oum', 'number',
            'unit_cost', 'amt_expense', 'procure_method', 'remarks'],
    widgets={

    },
    extra=1,
    can_delete=False
)


class IsolationConstructionExependitureForm(forms.ModelForm):

    class Meta:
        model = IsolationConstructionExependiture
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
