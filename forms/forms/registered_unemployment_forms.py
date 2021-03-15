from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden,ButtonHolder,Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.registered_unemployment import RegisteredUnemployment, RegisteredUnemploymentLine


class RegisteredUnemploymentLineForm(forms.ModelForm):

    class Meta:
        model = RegisteredUnemploymentLine
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


RegisteredUnemploymentFormSet = inlineformset_factory(
    RegisteredUnemployment, RegisteredUnemploymentLine, form=RegisteredUnemploymentLineForm,
    fields=['fiscal_year', 'unemployed_registered_num', 'employed_registered_num', 'employment_provided_total_days',
            'employment_provided_days_per_person', 'reg_unemployment_line'],
    extra=1,
    can_delete=True
)


class RegisteredUnemploymentForm(forms.ModelForm):

    class Meta:
        model = RegisteredUnemployment
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
            ButtonHolder(Submit('submit', 'save')),
            
            )
        )
