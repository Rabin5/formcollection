from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.company import Importer


class ImporterForm(ModelForm):
    class Meta:
        model = Importer
        fields = (
            'name', 'date_establishment',
            'country', 'province', 'district', 'local_level', 'ward',
        )
