from django.core.exceptions import ValidationError
from django.db.models import fields
from django import forms

from crispy_forms.helper import FormHelper

from collection.models.internal_affairs_form_collection import InternalAffairFormCollection
from master_data import models

class InternalAffairsFormCollectionForm(forms.ModelForm):
    
    class Meta:
        model = InternalAffairFormCollection
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
        Create respective Internal Affairs Body, if it does not exist
        """
        instance = super().save(commit=False)
        try:
            ia_name = 'आन्तरिक मामिला तथा कानून मन्त्रालय, ' + instance.province.name
            body = models.GovernmentBody.objects.get(name=ia_name)
        except models.GovernmentBody.DoesNotExist:
                body = models.GovernmentBody.objects.create(
                    name=ia_name,
                    type=models.GovernmentBodyType.objects.get(name='आन्तरिक मामिला तथा कानून मन्त्रालय'),
                    province=instance.province,
                )   
        
        instance.body = body
        instance.save()
        return instance