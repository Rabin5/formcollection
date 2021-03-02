from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden,ButtonHolder,Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.procedure_guide import ProcedureGuide, ProcedureGuideLine


class ProcedureGuideLineForm(forms.ModelForm):

    class Meta:
        model = ProcedureGuideLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class']='form-control'
            # if field.widget.input_type == 'select':
            #     field.widget.attrs.update({'class': 'select_class'})
            # else:
            #     field.widget.attrs['class'] = 'form-control'


ProcedureGuideFormSet = inlineformset_factory(
    ProcedureGuide, ProcedureGuideLine, form=ProcedureGuideLineForm,
    fields=['desc', 'act', 'rules',
            'procedure_desc', 'directory', 'norms', 'total', 'procedure_guide'],
    extra=1,
    can_delete=True
)


class ProcedureGuideForm(forms.ModelForm):

    class Meta:
        model = ProcedureGuide
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
