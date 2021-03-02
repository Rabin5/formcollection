from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden,ButtonHolder,Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.recover_amount import RecoverAmount,RecoverAmountLine


class RecoverAmountLineForm(forms.ModelForm):
    class Meta:
        model =RecoverAmountLine
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


RecoverAmountFormSet = inlineformset_factory(
   RecoverAmount,RecoverAmountLine, form=RecoverAmountLineForm,
    fields=['contractor', 'income_name', 'prev_year_rem_amt',
            'this_year_recover_amt', 'cur_rem_amt','rem_recover_amt','total_rem_amt','recover_amount'],
    extra=1,
    can_delete=True
)


class RecoverAmountForm(forms.ModelForm):

    class Meta:
        model =RecoverAmount
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
            ButtonHolder(Submit('submit', 'save')),
             
            ) 
        )