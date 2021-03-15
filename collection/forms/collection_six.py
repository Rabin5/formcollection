
from django.core.exceptions import ValidationError
from django.db.models import fields
from django import forms

from crispy_forms.helper import FormHelper

from collection.models.collection_six import CollectionSixFormCollection
from master_data.models.government import GovernmentBody, GovernmentBodyType
from master_data import models


class CollectionSixForm(forms.ModelForm):

    class Meta:
        model = CollectionSixFormCollection
        fields = ('province', 'district', 'local_level', 'fiscal_year')
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

    def save(self, commit=True):
        """
        Create respective Local Level Body, if it does not exist
        """
        instance = super().save(commit=False)
        try:
            body = models.GovernmentBody.objects.get(name=instance.local_level)
        except models.GovernmentBody.DoesNotExist:
            body = models.GovernmentBody.objects.create(
                name=instance.local_level.name,
                type=models.GovernmentBodyType.objects.get(
                    name='स्थानीय तह'),
                province=instance.province,
                district=instance.district,
                local_level=instance.local_level,
            )

        instance.body = body
        instance.save()
        return instance
