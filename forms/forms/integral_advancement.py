from django.db.models import aggregates
from master_data.widgets import NepaliDateInput
from django import forms
from django.forms import widgets
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models.integral_advancement import IntegralAdvancement, IntegralAdvancementLine
from master_data.widgets import NepaliDateInput
import nepali_datetime


class IntegralAdvancementLineForm(forms.ModelForm):
    class Meta:
        model = IntegralAdvancementLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    #     for _, field in self.fields.items():
    #         if field.widget.input_type == 'select':
    #             field.widget.attrs.update({'class': 'select_class'})
    #         else:
    #             field.widget.attrs['class'] = 'form-control'


IntegralAdvancementFormSet = inlineformset_factory(
    IntegralAdvancement, IntegralAdvancementLine, form=IntegralAdvancementLineForm,
    fields=['desc', 'remaining_advance', 'cancelled_amount',
            'remaining_amount', 'added_amount', 'total', 'integral_advancement'],
    extra=1,
    can_delete=True
)


class IntegralAdvancementForm(forms.ModelForm):

    class Meta:
        model = IntegralAdvancement
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
            )
        )
