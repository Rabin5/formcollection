from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm

from collection.models.cov_hos_form_collection import CovHosFormCollection

class CovHosFormCollectionForm(ModelForm):
    class Meta:
        model = CovHosFormCollection
        fields = '__all__'
        exclude = ('user', )
        # fields = ['state', 'med_exp', 'risk_allowance', 'status']
        
