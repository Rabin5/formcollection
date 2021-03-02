from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, Submit, ButtonHolder

from forms.custom_layout_object import Formset
from forms.models.teacherdesignation import TeacherDesignationLine, TeacherDesignation
from django.forms.models import inlineformset_factory
from forms.fields import ModelChoiceFieldWithCreate


class TeacherDesginationForm(forms.ModelForm):
    class Meta:
        model = TeacherDesignationLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


TeacherDesginationFormSet = inlineformset_factory(
    TeacherDesignation, TeacherDesignationLine, form=TeacherDesginationForm,
    fields=['school', 'num_vacancy', 'num_vacancy_filled',
            'num_temp_filled', 'num_student'],
    extra=1,
    can_delete=True

)


class TeacherDesginationLineForm(forms.ModelForm):
    class Meta:
        model = TeacherDesignation
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
            )
        )
