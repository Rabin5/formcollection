from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.designation import *


class DesignationForm(ModelForm):
    class Meta:
        model = Designation
        fields = ['name', ]
     