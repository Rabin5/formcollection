from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Div, Fieldset, Hidden, ButtonHolder, Submit, Layout, Row
from django import forms
from django.forms.models import inlineformset_factory

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models import IsolationConstructionExependiture, IsolationConstructionExependitureLine, Product, UnitOfMeasure, ProcurementMethod


class IsolationConstructionExependitureLineForm(forms.ModelForm):
    product = ModelChoiceFieldWithCreate(queryset=Product.objects.all(), label='खरिद भएका सामग्री', blank=False, save_to_field='name')
    uom = ModelChoiceFieldWithCreate(queryset=UnitOfMeasure.objects.all(), label='इकाई', blank=False, save_to_field='name')
    procure_method = ModelChoiceFieldWithCreate(queryset=ProcurementMethod.objects.all(), label='खरिद विधि', blank=False, save_to_field='name')

    class Meta:
        model = IsolationConstructionExependitureLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


IsolationConstructionExependitureFormSet = inlineformset_factory(
    IsolationConstructionExependiture, IsolationConstructionExependitureLine, form=IsolationConstructionExependitureLineForm,
    fields=['product', 'uom', 'number',
            'unit_cost', 'amt_expense', 'procure_method', 'remarks'],
    widgets={

    },
    extra=1,
    can_delete=True
)


class IsolationConstructionExependitureForm(forms.ModelForm):

    class Meta:
        model = IsolationConstructionExependiture
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
