from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden
from forms.custom_layout_object import Formset
from forms.models.judicialcommittee import JudicialCommittee, JudicialCommitteeLine


class JudicialCommitteeForm(forms.ModelForm):
    class Meta:
        model = JudicialCommitteeLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


JudicialCommitteeFormSet = inlineformset_factory(
    JudicialCommittee, JudicialCommitteeLine, form=JudicialCommitteeForm,
    fields=['complaint_type', 'prev_remaining', 'current_addition',
            'total', 'summed_up', 'remaining', 'desc'],
    extra=1,
    can_delete=True
)


class JudicialCommitteeFormLine(forms.ModelForm):

    class Meta:
        model = JudicialCommittee
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
