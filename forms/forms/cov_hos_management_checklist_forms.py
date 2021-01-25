from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.models import CovidHospitalManagementChecklist, CovidHospitalManagementChecklistLine

class CovidHospitalManagementChecklistLineForm(forms.ModelForm):

    # is_yes = forms.CheckboxSelectMultiple(choices=((0, True), (1, False)))

    class Meta:
        model = CovidHospitalManagementChecklistLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    


CovidHospitalManagementChecklistLineFormSet = inlineformset_factory(
    CovidHospitalManagementChecklist, CovidHospitalManagementChecklistLine, form=CovidHospitalManagementChecklistLineForm,
    fields=['cov_hos_management', 'description', 'is_yes', 'remarks'],
    widgets = {
        # 'is_yes': forms.CheckboxSelectMultiple(choices=((0, True),(1, False)))
    },
    extra=1,
    can_delete=False
)


class CovidHospitalManagementChecklistForm(forms.ModelForm):

    class Meta:
        model = CovidHospitalManagementChecklist
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
                Column('hospital', css_class='col-md-6 mb-0'),
                css_class='form-row'
                ),
            Div(
                Fieldset('',
                    Formset('lines')
                ),
            )
        )