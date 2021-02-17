from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.work_nature import *


class WorkNatureForm(ModelForm):
    class Meta:
        model = WorkNature
        fields = ['name', ]
     