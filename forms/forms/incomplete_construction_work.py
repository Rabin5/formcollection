from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate, NepaliDateField
from forms.models.incomplete_construction_work import IncompleteConstructionWork, IncompleteConstructionWorkLine, ConstructionCompany


class IncompleteConstructionWorkLineForm(forms.ModelForm):
    construction_company = ModelChoiceFieldWithCreate(queryset=ConstructionCompany.objects.all(), label='निर्माण व्यवसायी', blank=False, save_to_field='name')
    agreement_date = NepaliDateField(label='सम्झौता मिति')
    estimated_completion_date = NepaliDateField(label='सम्पन्न गर्नुपर्ने मिति')

    class Meta:
        model = IncompleteConstructionWorkLine
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


IncompleteConstructionWorkFormSet = inlineformset_factory(
    IncompleteConstructionWork, IncompleteConstructionWorkLine, form=IncompleteConstructionWorkLineForm,
    fields=['construction_work', 'construction_company', 'agreement_date',
            'estimated_completion_date', 'expense', 'progress',
            'incomplete_construction_work_line'],
    extra=1,
    can_delete=True
)


class IncompleteConstructionWorkForm(forms.ModelForm):

    class Meta:
        model = IncompleteConstructionWork
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
                css_class='form-row'
                ),
            Div(
                Fieldset('',
                    Formset('lines')
                ),
            )
        )