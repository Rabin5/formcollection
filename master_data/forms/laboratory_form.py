from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.company import Laboratory


class LaboratoryForm(ModelForm):
    class Meta:
        model = Laboratory
        fields = '__all__'
