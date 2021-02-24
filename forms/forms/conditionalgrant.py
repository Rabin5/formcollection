from django import forms
from forms.models.additionalconvenience import AdditionalConvenience, AdditionalConvenienceLine
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from forms.custom_layout_object import Formset
from crispy_forms.layout import Layout, Field, Fieldset, Div, ButtonHolder, Submit, Hidden, Row, Column
from forms.models.conditionalgrant import ConditionalGrantLine, ConditionalGrant
from forms.fields import ModelChoiceFieldWithCreate
from master_data.models.grant_type import GrantType


class ConditionalGrantForm(forms.ModelForm):
    grant_type = ModelChoiceFieldWithCreate(queryset=GrantType.objects.all(
    ), label='अनुदानको किसिम', blank=False, save_to_field='name')

    class Meta:
        model = ConditionalGrant
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


ConditionalGrantFormSet = inlineformset_factory(
    ConditionalGrant, ConditionalGrantLine, form=ConditionalGrantForm,
    fields=[
        'grant_type', 'total_grant', 'expense',
        'freeze_amount', 'remarks'], extra=1, can_delete=True)


class ConditionalGrantFormLine(forms.ModelForm):

    class Meta:
        model = ConditionalGrant
        exclude = ('create_user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_id = 'form_to_submit'
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-md-3 create-label'
        # self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Hidden('next_state', 'next'),
            Row(Column('body', css_class='col-md-6 mb-0'),
                Column('state', css_class='col-md-6 mb-0'),
                css_class='form-row'
                ),
            Div(Fieldset('', Formset('lines')),
                ButtonHolder(Submit('submit', 'save')),
                )

        )
