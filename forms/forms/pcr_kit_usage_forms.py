from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models import PcrKitUsage, PcrKitUsageLine, Laboratory   

class PcrKitUsageLineForm(forms.ModelForm):
    laboratory = ModelChoiceFieldWithCreate(queryset=Laboratory.objects.all(), label='प्रयोगशालाको नाम', blank=False, save_to_field='name')

    class Meta:
        model = PcrKitUsageLine
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


PcrKitUsageLineFormSet = inlineformset_factory(
    PcrKitUsage, PcrKitUsageLine, form=PcrKitUsageLineForm,
    fields=['pcr_kit_usage', 'laboratory', 'num_kit_received', 'num_kit_expensed', 'num_kit_available', 'num_tests', 'num_wasted'],
    widgets = {

    },
    extra=1,
    can_delete=True
)


class PcrKitUsageForm(forms.ModelForm):

    class Meta:
        model = PcrKitUsage
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
