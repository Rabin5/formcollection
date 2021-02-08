from django.core.exceptions import ValidationError
from django.db.models import fields
from django import forms

from crispy_forms.helper import FormHelper

from collection.models.province_form_collection import ProvinceFormCollection
from master_data import models

class ProvinceFormCollectionForm(forms.ModelForm):
    
    class Meta:
        model = ProvinceFormCollection
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
        Create respective Province Body, if it does not exist
        """
        instance = super().save(commit=False)
        try:
            body = models.GovernmentBody.objects.get(name=instance.province.name)
        except models.GovernmentBody.DoesNotExist:
                body = models.GovernmentBody.objects.create(
                    name=instance.province.name,
                    type=models.GovernmentBodyType.objects.get(name='प्रदेश सरकार'),
                    province=instance.province,
                )   
        
        instance.body = body
        instance.save()
        return instance