from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden,ButtonHolder,Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.designation_vacancy import DesignationVacancy, DesignationVacancyLine


class DesignationVacancyLineForm(forms.ModelForm):

    class Meta:
        model = DesignationVacancyLine
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


DesignationVacancyFormSet = inlineformset_factory(
    DesignationVacancy, DesignationVacancyLine, form=DesignationVacancyLineForm,
    fields=['designation', 'total', 'num_internal',
            'num_union', 'num_filled', 'remaining_vacancy','num_former_body','remarks','designation_vacancy'],
    extra=1,
    can_delete=True
)


class DesignationVacancyForm(forms.ModelForm):

    class Meta:
        model = DesignationVacancy
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