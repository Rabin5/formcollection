from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.convenience_type import *


class ConvenienceTypeForm(ModelForm):
    class Meta:
        model = ConvenienceType
        fields = ['name', ]
     
     