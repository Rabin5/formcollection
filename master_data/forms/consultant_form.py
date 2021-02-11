from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.consultant import *

class ConsultantForm(ModelForm):
    class Meta:
        model = Consultant
        fields = ['name', ]