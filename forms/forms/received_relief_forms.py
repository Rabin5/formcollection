from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, Submit, ButtonHolder

from forms.custom_layout_object import Formset
from forms.models import ReceivedReliefDetail, ReceivedReliefDetailLine


class ReceivedReliefDetailLineForm(forms.ModelForm):

    class Meta:
        model = ReceivedReliefDetailLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


ReceivedReliefDetailFormSet = inlineformset_factory(
    ReceivedReliefDetail, ReceivedReliefDetailLine, form=ReceivedReliefDetailLineForm,
    fields=['provider', 'unit', 'qty_received', 'qty_distributed', 'relief_material', 'qty_remaining',
    'ward_relief'
            ],
    extra=1,
    can_delete=True
)


class ReceivedReliefDetailForm(forms.ModelForm):

    class Meta:
        model = ReceivedReliefDetail
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
