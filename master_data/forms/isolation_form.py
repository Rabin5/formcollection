from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.company import IsolationCenter


class IsolationCenterForm(ModelForm):
    class Meta:
        model = IsolationCenter
        fields = '__all__'
