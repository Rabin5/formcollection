from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models. expenditure_detail import ExpenditureDetail, ExpenditureDetailLine


class ExpenditureDetailLineForm(forms.ModelForm):

    class Meta:
        model = ExpenditureDetailLine
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


ExpenditureDetailFormSet = inlineformset_factory(
    ExpenditureDetail, ExpenditureDetailLine, form=ExpenditureDetailLineForm,
    fields=['grant_providing_body', 'grant_type', 'received_amount',
            'expensed_amount', 'remaining_amount','expenditure_detail'],
    extra=1,
    can_delete=True
)


class ExpenditureDetailForm(forms.ModelForm):

    class Meta:
        model = ExpenditureDetail
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
