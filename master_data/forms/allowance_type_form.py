from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.government import AllowanceType


class AllowanceTypeForm(ModelForm):
    class Meta:
        model = AllowanceType
        fields = '__all__'

  