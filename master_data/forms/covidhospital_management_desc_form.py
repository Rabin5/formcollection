from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.government import CovidHospitalManagementChecklistDescription

class CovidHospitalManagementChecklistDescriptionForm(ModelForm):
    class Meta:
        model = CovidHospitalManagementChecklistDescription
        fields = '__all__'
