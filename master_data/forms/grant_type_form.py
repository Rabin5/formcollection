from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.grant_type import *


class GrantTypeForm(ModelForm):
    class Meta:
        model = GrantType
        fields = ['name', ]

