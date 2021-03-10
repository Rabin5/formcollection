from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit
from forms.custom_layout_object import Formset
from forms.models.consumercommitteecons_desc import ConsumerCommitteeConstructionDescription, ConsumerCommitteeConstructionDescriptionLine


class ConsumercomConsDespForm(forms.ModelForm):
    class Meta:
        model = ConsumerCommitteeConstructionDescriptionLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


ConsumercomConsDespFormSet = inlineformset_factory(
    ConsumerCommitteeConstructionDescription, ConsumerCommitteeConstructionDescriptionLine, form=ConsumercomConsDespForm,
    fields=['program', 'total_expense', 'consumer_committee_expense',
            'construction_business_expense', 'consumercommitteeconstructiondescription_line'],
    extra=1,
    can_delete=True
)


class ConsumercomConsDespFormLine(forms.ModelForm):

    class Meta:
        model = ConsumerCommitteeConstructionDescription
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
