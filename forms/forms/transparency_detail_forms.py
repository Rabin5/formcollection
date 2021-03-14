from django import forms
from django.forms.forms import Form
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.transparency_detail import TransparencyDetail, TransparencyDetailLine


class TransparencyDetailLineForm(forms.ModelForm):
    
    class Meta:
        model = TransparencyDetailLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


TransparencyDetailLineFormSet = inlineformset_factory(
    TransparencyDetail, TransparencyDetailLine, form=TransparencyDetailLineForm,
    fields=['details', 'is_true', 'remarks',
            'transparency_detail_line'],
    extra=1,
    can_delete=False
)


class TransparencyDetailForm(forms.ModelForm):

    class Meta:
        model = TransparencyDetail
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
                Fieldset('', Formset('lines')
                         ),
                # ButtonHolder(Submit('submit', 'save')),
            )
        )
