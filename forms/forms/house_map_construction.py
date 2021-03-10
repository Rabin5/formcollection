from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models.house_map_construction import HouseMapConstruction, HouseMapConstructionLine
from master_data.widgets import NepaliDateInput


class HouseMapConstructionFormLine(forms.ModelForm):

    class Meta:
        model = HouseMapConstructionLine
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


HouseMapConstructionLineFormset = inlineformset_factory(
    HouseMapConstruction, HouseMapConstructionLine, form=HouseMapConstructionFormLine,
    fields=['application_count', 'temporary_permission', 'prev_year_approved_num',
            'current_year_approved_num', 'total', 'remarks'],
    extra=1,
    can_delete=True
)


class HouseMapConstructionForm(forms.ModelForm):

    class Meta:
        model = HouseMapConstruction
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
            Row(
                Column('fiscal_year_from', css_class='col-md-3 mb-0'),
                Column('fy_month_from', css_class='col-md-3 mb-0'),
                Column('fiscal_year_to', css_class='col-md-3 mb-0'),
                Column('fy_month_to', css_class='col-md-3 mb-0'),
                css_class='form-row'
            ),
            Div(
                Fieldset('',
                         Formset('lines')
                         ),
            )
        )
