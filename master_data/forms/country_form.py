from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.address import Country


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
