from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, Submit, ButtonHolder

from forms.custom_layout_object import Formset
from forms.models.recommend_training_center import RecommendTrainingCenter, RecommendTrainingCenterLine


class RecommendTrainingCenterLineForm(forms.ModelForm):

    class Meta:
        model = RecommendTrainingCenterLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


RecommendTrainingCenterFormSet = inlineformset_factory(
    RecommendTrainingCenter, RecommendTrainingCenterLine, form=RecommendTrainingCenterLineForm,
    fields=['training_subject', 'training_center', 'num_employed', 'total_recommend', 'employed_days',
            'employed_days', 'ecommendtrainingcenter_line'
            ],
    extra=1,
    can_delete=True
)


class RecommendTrainingCenterForm(forms.ModelForm):

    class Meta:
        model = RecommendTrainingCenter
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
