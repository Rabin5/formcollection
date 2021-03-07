from django.forms import ModelForm

from master_data.models.employer_type import *


class EmployerTypeForm(ModelForm):
    class Meta:
        model = EmployerType
        fields = ['name', ]
     