# from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from master_data.models.government import AllowanceType


class AllowanceTypeForm(ModelForm):
    class Meta:
        model = AllowanceType
        fields = '__all__'

  