from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.address import District, Province
from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from master_data.custom_layout_object import Formset


class DistrictForm(forms.ModelForm):
    name = forms.CharField(label='', required=False)

    class Meta:
        model = District
        exclude = ()


DistrictFormFormSet = inlineformset_factory(
    Province, District, form=DistrictForm,
    fields=['name', ],
    extra=1,
    can_delete=True
)


class DistrictFormLine(forms.ModelForm):
    class Meta:
        model = Province
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-inline'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Fieldset('जिल्लाहरुको नाम',
                         Formset('lines')
                         ),


            )
        )
