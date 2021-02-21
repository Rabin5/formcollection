from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.vehicle import *


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', ]
     