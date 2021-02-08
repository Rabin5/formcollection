from django.core.exceptions import ValidationError
from django.db.models import fields
from django import forms

from crispy_forms.helper import FormHelper

from collection.models.chief_minister_form_collection import ChiefMinisterOfficeFormCollection
from master_data import models

class ChiefMinisterOfficeFormCollectionForm(forms.ModelForm):
    
    class Meta:
        model = ChiefMinisterOfficeFormCollection
        fields = ('province', 'fiscal_year')
        exclude = ('user', )
        widgets = {
            'province': forms.Select(attrs={'autocomplete': 'off'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'create_form'
    
    def save(self, commit=True):
        """
        Create respective Chief Ministers Office Body, if it does not exist
        """
        instance = super().save(commit=False)
        try:
            ia_name = 'मुख्यमन्त्री तथा मन्त्रीपरिषदको कार्यालय, ' + instance.province.name
            body = models.GovernmentBody.objects.get(name=ia_name)
        except models.GovernmentBody.DoesNotExist:
                body = models.GovernmentBody.objects.create(
                    name=ia_name,
                    type=models.GovernmentBodyType.objects.get(name='मुख्यमन्त्री तथा मन्त्रीपरिषदको कार्यालय'),
                    province=instance.province,
                )   
        
        instance.body = body
        instance.save()
        return instance