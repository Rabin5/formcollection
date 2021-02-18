from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.procurement_auditor import ProcurementAuditorLine, ProcurementAuditor, SubHeader, WorkNature


class ProcurementAuditorLineForm(forms.ModelForm):
    sub_header = ModelChoiceFieldWithCreate(queryset=SubHeader.objects.all(), label='उपशीर्षकको नाम', blank=False, save_to_field='name')
    work_nature = ModelChoiceFieldWithCreate(queryset=WorkNature.objects.all(), label='कामको प्रकृति', blank=False, save_to_field='name')

    class Meta:
        model = ProcurementAuditorLine
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


ProcurementAuditorFormSet = inlineformset_factory(
    ProcurementAuditor, ProcurementAuditorLine, form=ProcurementAuditorLineForm,
    fields=['sub_header', 'work_nature', 'amt_expense_estimate',
            'num_piece', 'amt_expense', 'procurement_auditor_line'],
    extra=1,
    can_delete=True
)


class ProcurementAuditorForm(forms.ModelForm):

    class Meta:
        model = ProcurementAuditor
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