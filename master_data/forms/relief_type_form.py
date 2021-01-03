from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.government import ReliefType

class ReliefTypeForm(ModelForm):
    class Meta:
        model = ReliefType
        fields = '__all__'
