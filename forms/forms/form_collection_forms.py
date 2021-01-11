from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from forms.models.form_collection import FormCollection

class FormCollectionForm(ModelForm):
    class Meta:
        model = FormCollection
        fields = {} 
        # fields = ['state', 'med_exp', 'risk_allowance', 'status']
        
