from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.company import Laboratory


class LaboratoryForm(ModelForm):
    class Meta:
        model = Laboratory
        fields = (
            'name', 'date_establishment', 'capacity_daily_test',
            'country', 'province', 'district', 'local_level', 'ward',
        )
