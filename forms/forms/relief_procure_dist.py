from django import forms
from django.forms.forms import Form
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models.reliefprocuredistribution import ReliefProcureDistribution, ReliefProcureDistributionLine


class ReliefProcureDistributionLineForm(forms.ModelForm):

    class Meta:
        model = ReliefProcureDistributionLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            # if field.widget.input_type != 'select':
            field.widget.attrs['class'] = 'form-control'


ReliefProcureDistributionFormSet = inlineformset_factory(
    ReliefProcureDistribution, ReliefProcureDistributionLine, form=ReliefProcureDistributionLineForm,
    fields=['product', 'uom', 'qty_purchase',
            'rate', 'amt_total', 'qty_distributed', 'qty_remaining', 'has_quality_complaint'],
    extra=1,
    can_delete=False
)


class ReliefProcureDistributionForm(forms.ModelForm):

    class Meta:
        model = ReliefProcureDistribution
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
