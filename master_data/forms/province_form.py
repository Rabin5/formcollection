from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.address import Province


class ProvinceForm(ModelForm):
    class Meta:
        model = Province
        fields = '__all__'
