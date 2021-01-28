from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Div, Fieldset, Hidden, ButtonHolder, Submit, Layout, Row
from django import forms
from django.forms.forms import Form
from django.forms.models import inlineformset_factory
from forms.custom_layout_object import Formsett
from forms.models.districtcovidmanagement import DistrictCovidManagement, DisctrictQuarantineManagementLine, DistrictIsolationManagementLine, DistrictLabTestLine


class DistrictQuarantineManagementLineForm(forms.ModelForm):

    class Meta:
        model = DisctrictQuarantineManagementLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DistrictIsolationManagementLineForm(forms.ModelForm):

    class Meta:
        model = DistrictIsolationManagementLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DistrictLabTestLineForm(forms.ModelForm):

    class Meta:
        model = DistrictLabTestLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


DistrictCovidQuaManagementFormSet = inlineformset_factory(
    DistrictCovidManagement, DisctrictQuarantineManagementLine, form=DistrictQuarantineManagementLineForm,
    fields=['district', 'num_prepared_quarantine', 'num_quarantined_person',
            'num_home_quarantined_person', 'num_insufficient_bed', ],
    extra=1,
    can_delete=False
)
DistrictCovidIsolManagementFormSet = inlineformset_factory(
    DistrictCovidManagement, DistrictIsolationManagementLine, form=DistrictIsolationManagementLineForm,
    fields=['district', 'num_prepared_icu', 'num_prepared_bed',
            'num_infected_person', 'num_isolated_person', 'num_home_isolated_person'],
    extra=1,
    can_delete=False
)

DistrictCovidLabtTestManagementFormSet = inlineformset_factory(
    DistrictCovidManagement, DistrictLabTestLine, form=DistrictLabTestLineForm,
    fields=['district', 'num_rdt_tests', 'num_rdt_results_received',
            'num_rdt_positive_results', 'num_pcr_tests', 'num_pcr_results_received',
            'num_pcr_positive_results', 'num_pcr_contract_trace', 'num_covid_treated_patients',
            'num_covid_recovered_patients', 'num_isolation_treatments', 'num_icu_treatments',
            'num_covid_deaths'],
    extra=1,
    can_delete=False
)


class DistrictCovidManagementForm(forms.ModelForm):

    class Meta:
        model = DistrictCovidManagement
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
                Fieldset('आईसोलेशनमा व्यवस्थापन', Formsett(
                    'isolationlines'), id='first_fieldset'),
                Fieldset('क्वारेन्टीन व्यवस्थापन', Formsett('quarentinelines'),
                         id='second_fieldset'),
                Fieldset('ल्याब व्यवस्थापन', Formsett(
                    'labtestlines'), id='third_fieldset'),
            )

        )
