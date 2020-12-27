from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.address import District


class DistrictForm(ModelForm):
    class Meta:
        model = District
        fields = '__all__'
