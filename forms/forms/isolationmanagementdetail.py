from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models import IsolationManagementDetailLine, IsolationManagementDetail


class IsolationDetailManagementLineForm(forms.ModelForm):

    class Meta:
        model = IsolationManagementDetailLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


IsolationManagementDetailFormSet = inlineformset_factory(
    IsolationManagementDetail, IsolationManagementDetailLine, form=IsolationDetailManagementLineForm,
    fields=['isolationcenter', 'cost_construction', 'num_bed',
            'max_num_daily_stay', 'num_stayed_till_fy_end', 'expense_operations'],
    widgets={

    },
    extra=1,
    can_delete=False
)


class IsolationManagementDetailForm(forms.ModelForm):

    class Meta:
        model = IsolationManagementDetail
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
