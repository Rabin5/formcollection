from django import forms
from django.forms.models import inlineformset_factory

import nepali_datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate, NepaliDateField
from forms.models.covidhospitaldetail import CovidHospitalDetail, CovidHospitalDetailLine, CovidHospital


class CovidHospitalDetailLineForm(forms.ModelForm):
    covidhospital = ModelChoiceFieldWithCreate(queryset=CovidHospital.objects.all(), label='डेडिकेटेड अस्पतालको नाम र स्थान', blank=False, save_to_field='name')
    date_announcement = NepaliDateField(label='कोभिड अस्पताल घोषणा भएको मिति')

    class Meta:
        model = CovidHospitalDetailLine
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
        
        # Convert date to Nepali datetime before displaying
        date_announcement = self.initial.get('date_announcement')
        if date_announcement:
            self.initial['date_announcement'] = nepali_datetime.date.from_datetime_date(date_announcement).strftime('%d/%m/%Y')
    
    def save(self, commit=True):
        instance = super().save()
        instance.covidhospital.date_announcement = instance.date_announcement
        instance.covidhospital.save()
        return instance


CovidHospitaldetatilFormSet = inlineformset_factory(
    CovidHospitalDetail, CovidHospitalDetailLine, form=CovidHospitalDetailLineForm,
    fields=['covidhospital', 'date_announcement', 'announce_time_health_workers', 'announce_time_beds',
            'announce_time_icu', 'announce_time_ventilators', 'added_health_workers', 'added_beds', 'added_icu', 'added_ventilators', 'num_treated_patients', 'expense_treatment'],
    extra=1,
    can_delete=False
)


class CovidHospitalDetailForm(forms.ModelForm):

    class Meta:
        model = CovidHospitalDetail
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
