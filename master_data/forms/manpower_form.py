from django.forms import ModelForm
from django.core.exceptions import ValidationError
from master_data.models.government import Manpower


class ManpowerForm(ModelForm):
    class Meta:
        model = Manpower
        fields = '__all__'
