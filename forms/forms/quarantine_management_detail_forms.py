from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models import QuarantineManagementDetail, QuarantineManagementDetailLine, QuanrantineCenter

class QuarantineManagementDetailLineForm(forms.ModelForm):
    quarantine_center = ModelChoiceFieldWithCreate(queryset=QuanrantineCenter.objects.all(), label='यस निकायले तयार वा सञ्चालन गरेको क्वारेन्टिन/होल्डिङ सेन्टरको नाम', blank=False, save_to_field='name')

    class Meta:
        model = QuarantineManagementDetailLine
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
            


QuarantineManagementDetailLineFormSet = inlineformset_factory(
    QuarantineManagementDetail, QuarantineManagementDetailLine, form=QuarantineManagementDetailLineForm,
    fields=['quarantine_management', 'quarantine_center', 'cost_construction', 'num_bed', 'max_num_daily_stay', 'num_stayed_till_fy_end', 'expense_operations'],
    widgets = {
    },
    extra=1,
    can_delete=False
)


class QuarantineManagementDetailForm(forms.ModelForm):

    class Meta:
        model = QuarantineManagementDetail
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