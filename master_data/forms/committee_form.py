from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.government import Committee

class CommitteeForm(ModelForm):
    class Meta:
        model = Committee
        fields = '__all__'
