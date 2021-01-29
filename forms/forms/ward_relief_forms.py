from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, Submit, ButtonHolder

from forms.custom_layout_object import Formset
from forms.models import WardReliefProcureDistribution, WardReliefProcureDistributionLine


class WardReliefProcureDistributionLineForm(forms.ModelForm):

    class Meta:
        model = WardReliefProcureDistributionLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


WardReliefProcureDistributionFormSet = inlineformset_factory(
    WardReliefProcureDistribution, WardReliefProcureDistributionLine, form=WardReliefProcureDistributionLineForm,
    fields=['ward_num', 'amt_relief_material_purchase', 'procure_method', 'relief_beneficiary_family', 'num_relief_benefitted', 'remarks'
            ],
    extra=1,
    can_delete=False
)


class WardReliefProcureDistributionForm(forms.ModelForm):

    class Meta:
        model = WardReliefProcureDistribution
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
