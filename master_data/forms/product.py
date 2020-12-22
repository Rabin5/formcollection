from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from master_data.models.product import *


class ProdForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'type', 'uom']
    
class UomForm(ModelForm):
    class Meta:
        model = UnitOfMeasure
        fields = ['name', ]