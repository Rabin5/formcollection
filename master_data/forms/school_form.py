from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.school import *


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['name', ]
     