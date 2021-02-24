from django import forms
from django.forms.forms import Form
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.service_flow import ServiceFlow, ServiceFlowLine


class ServiceFlowForm(forms.ModelForm):
    pass
    # office_bearer = ModelChoiceFieldWithCreate(queryset=OfficeBearer.objects.all(
    # ), label='जोखिम भत्ता पाउने पदाधिकारी', blank=False, save_to_field='title')
    # allowance_type = ModelChoiceFieldWithCreate(queryset=AllowanceType.objects.all(
    # ), label='भत्ताको प्रकार', blank=False, save_to_field='name')

    class Meta:
        model = ServiceFlowLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


ServiceFlowLineFormSet = inlineformset_factory(
    ServiceFlow, ServiceFlowLine, form=ServiceFlowForm,
    fields=['description', 'application_count', 'recommendation_count',
            'remarks'],
    extra=1,
    can_delete=True
)


class ServiceFlowFormLine(forms.ModelForm):

    class Meta:
        model = ServiceFlow
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
                Fieldset('', Formset('lines')
                         ),
                ButtonHolder(Submit('submit', 'save')),
            )
        )
