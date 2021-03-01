from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.peski_bibaran import *


class PeskiBibaranForm(ModelForm):
    class Meta:
        model = PeskiBibaran
        fields = ['desc', ]
     