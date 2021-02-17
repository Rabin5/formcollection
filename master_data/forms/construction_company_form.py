from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.construction_company import *


class ConstructionCompanyForm(ModelForm):
    class Meta:
        model = ConstructionCompany
        fields = ['name', ]
