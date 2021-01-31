from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.rdttestdetail import RdtTestDetailLine, RdtTestDetail, Laboratory


class RdtTestLineForm(forms.ModelForm):
    laboratory = ModelChoiceFieldWithCreate(queryset=Laboratory.objects.all(), label='ल्यावको नाम र स्थान', blank=False, save_to_field='name')
    class Meta:
        model = RdtTestDetailLine
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


RdtTestFormSet = inlineformset_factory(
    RdtTestDetail, RdtTestDetailLine, form=RdtTestLineForm,
    fields=['laboratory', 'num_tested_fy_end', 'num_tested_pcr',
            'expense_rdt_test', ],
    extra=1,
    can_delete=True
)


class RdtTestForm(forms.ModelForm):

    class Meta:
        model = RdtTestDetail
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