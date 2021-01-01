from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm
from master_data.widgets import NepaliDateInput
import nepali_datetime

from master_data.models.government import *


class GovernmentBodyTypeForm(ModelForm):
    class Meta:
        model = GovernmentBodyType
        fields = ['name', 'parent']


class GovernmentBodyForm(ModelForm):
    class Meta:
        model = GovernmentBody
        fields = ['name', 'type', 'parent', 'covid_hospital']
        
