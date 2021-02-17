from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.sub_header import *


class SubHeaderForm(ModelForm):
    class Meta:
        model = SubHeader
        fields = ['name', ]
     