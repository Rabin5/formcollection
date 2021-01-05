from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.company import Location


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
