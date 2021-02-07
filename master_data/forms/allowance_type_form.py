# from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from master_data.models.government import AllowanceType


class AllowanceTypeForm(ModelForm):
    class Meta:
        model = AllowanceType
        fields = '__all__'

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     print(name)
    #     name_check = AllowanceType.objects.filter(name=name)
    #     if name_check.exists():
    #         raise forms.ValidationError("Title already exists")
    #     return name
