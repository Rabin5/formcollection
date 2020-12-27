from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.address import LocalLevel


class LocallevelForm(ModelForm):
    class Meta:
        model = LocalLevel
        fields = '__all__'
