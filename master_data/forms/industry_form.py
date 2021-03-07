from django.forms import ModelForm

from master_data.models.industry import *


class IndustryForm(ModelForm):
    class Meta:
        model = Industry
        fields = ['name', ]
     
     