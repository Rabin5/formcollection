from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden,ButtonHolder,Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate, NepaliDateField
from forms.models.detail_to_employer import DetailToEmployer, DetailToEmployerLine, EmployerType


class DetailToEmployerLineForm(forms.ModelForm):
    employer_type = ModelChoiceFieldWithCreate(queryset=EmployerType.objects.all(), label='रोजगारदाताको किसिम (सार्वजनिक आयोजन, निजी क्षेत्र, गैसस)', blank=False, save_to_field='name')
    employer_notified_date = NepaliDateField(label='रोजगारदातालाई जानकारी गराएको मिति')

    class Meta:
        model = DetailToEmployerLine
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


DetailToEmployerFormSet = inlineformset_factory(
    DetailToEmployer, DetailToEmployerLine, form=DetailToEmployerLineForm,
    fields=['employer_name_address', 'employer_type', 'employer_notified_date'
            'detail_to_emp_line'],
    extra=1,
    can_delete=True
)


class DetailToEmployerForm(forms.ModelForm):

    class Meta:
        model = DetailToEmployer
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
