from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.contractor import *


class ContractorForm(ModelForm):
    class Meta:
        model = Contractor
        fields = ['name', ]
     