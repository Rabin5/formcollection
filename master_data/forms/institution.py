from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.company import Institution


class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = (
            'name', 'date_establishment',
            'country', 'province', 'district', 'local_level', 'ward',
        )
