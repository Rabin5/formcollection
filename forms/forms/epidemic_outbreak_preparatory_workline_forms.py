from django import forms
from forms.models.epidemic_outbreak_preparatory_work import EpidemicOutbreakPreparatoryWorkLine, EpidemicOutbreakPreparatoryWork
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from forms.custom_layout_object import Formset
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit, Hidden, Row, Column


class EpidemicOutbreakPreparatoryWorkLineForm(forms.ModelForm):
    class Meta:
        model = EpidemicOutbreakPreparatoryWorkLine
        exclude = ()


EpidemicWorkLineFormSet = inlineformset_factory(EpidemicOutbreakPreparatoryWork, EpidemicOutbreakPreparatoryWorkLine, form=EpidemicOutbreakPreparatoryWorkLineForm, fields=[
                                                'preparation_work_to_do', 'major_activities', 'amt_expense'], extra=1, can_delete=False)


class EpidemicOutbreakPreparatoryWorkForm(forms.ModelForm):
    class Meta:
        model = EpidemicOutbreakPreparatoryWork
        exclude = ('create_user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
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
