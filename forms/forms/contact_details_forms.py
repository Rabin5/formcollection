from django import forms
from django.forms.models import inlineformset_factory

import nepali_datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from master_data.widgets import NepaliDateInput
from forms.models.contact_details import ContactDetails, ContactDetailsLine


class ContactDetailsLineForm(forms.ModelForm):
    designation_val = [
        (1, 'गाउपालिका अध्यक्ष्य वा नगरपालिका प्रमुख'),
        (2, 'लेखा प्रमुख'),
        (3, 'रोजगार संयोजक'),
        
    ]

    class Meta:
        model = ContactDetailsLine
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
    

ContactDetailsLineFormSet = inlineformset_factory(
    ContactDetails, ContactDetailsLine, form=ContactDetailsLineForm,
    fields=['designation', 'name', 'contact_number', 
    'email', 'contact_details_line'],
    extra=1,
    can_delete=True,
)


class ContactDetailsForm(forms.ModelForm):

    class Meta:
        model = ContactDetails
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
