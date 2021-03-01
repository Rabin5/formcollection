from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.project_type import *


class ProjectTypeForm(ModelForm):
    class Meta:
        model = ProjectType
        fields = ['name', ]
     