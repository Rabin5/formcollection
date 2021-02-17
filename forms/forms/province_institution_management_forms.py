from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Column,
    Div,
    Fieldset,
    Hidden,
    Layout,
    Row,
)
from django import forms
from django.forms.models import inlineformset_factory

from forms.custom_layout_object import Formset
from forms.models.province_institution_management import (
    ProvinceInstitutionManagement,
    ProvinceInstitutionManagementLine,
    Committee
)
from forms.fields import ModelChoiceFieldWithCreate


class ProvinceInstitutionManagementLineForm(forms.ModelForm):
    committee = ModelChoiceFieldWithCreate(
        queryset=Committee.objects.all(),
        label='प्रदेश तहमा गठन भएका समितिको नाम',
        blank=False,
        save_to_field='name'
    )

    class Meta:
        model = ProvinceInstitutionManagementLine
        exclude = ()
        widgets = {
            "major_works": forms.Textarea(attrs={"cols": 40, "rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


ProvinceInstitutionManagementLineFormSet = inlineformset_factory(
    ProvinceInstitutionManagement,
    ProvinceInstitutionManagementLine,
    form=ProvinceInstitutionManagementLineForm,
    fields=["province_institution_management", "committee", "major_works"],
    extra=1,
    can_delete=True,
)


class ProvinceInstitutionManagementForm(forms.ModelForm):
    class Meta:
        model = ProvinceInstitutionManagement
        fields = "__all__"
        exclude = ("create_user",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "form_to_submit"
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Hidden("next_state", "next"),
            Row(
                Column("body", css_class="col-md-6 mb-0"), css_class="form-row"
            ),
            Div(
                Fieldset("", Formset("lines")),
            ),
        )
