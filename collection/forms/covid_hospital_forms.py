from django.core.exceptions import ValidationError
from django.db.models import fields
from django import forms

from crispy_forms.helper import FormHelper

from collection.models.cov_hos_form_collection import CovHosFormCollection, CovidHospital
from master_data import models
from forms.fields import ModelChoiceFieldWithCreate

class CovHosFormCollectionForm(forms.ModelForm):
    hospital = ModelChoiceFieldWithCreate(queryset=CovidHospital.objects.all(), required=True, widget=forms.Select(attrs={'autocomplete': 'off'}))
    
    class Meta:
        model = CovHosFormCollection
        fields = ('province', 'district', 'local_level', 'hospital' , 'fiscal_year')
        exclude = ('user', )
        widgets = {
            'province': forms.Select(attrs={'autocomplete': 'off'}),
            'district': forms.Select(attrs={'autocomplete': 'off'}),
            'local_level': forms.Select(attrs={'autocomplete': 'off'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'create_form'
    
    def clean(self):
        """
        Update Covid Hospital details
        """
        self.cleaned_data = super().clean()
        hospital = self.cleaned_data.get('hospital')
        if hospital:
            province = self.cleaned_data.get('province')
            district = self.cleaned_data.get('district')
            local_level = self.cleaned_data.get('local_level')
            
            hospital.province = province
            hospital.district = district
            hospital.local_level = local_level
            hospital.save()
    
    def save(self, commit=True):
        """
        Create respective COVID Hospital, if it does not exist
        """
        instance = super().save(commit=False)
        try:
            body = models.GovernmentBody.objects.get(covid_hospital=instance.hospital)
        except models.GovernmentBody.DoesNotExist:
                body = models.GovernmentBody.objects.create(
                    name=instance.hospital.name,
                    type=models.GovernmentBodyType.objects.get(name='कोभिड अस्पताल'),
                    province=instance.province,
                    district=instance.district,
                    local_level=instance.local_level,
                    covid_hospital=instance.hospital,
                )
        
        instance.body = body
        instance.save()
        return instance