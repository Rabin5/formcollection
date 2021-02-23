from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.complaint_type import *

class ComplaintTypeForm(ModelForm):
    class Meta:
        model =ComplaintType
        fields =['name',]