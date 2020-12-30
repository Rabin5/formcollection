from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.government import OfficeBearer


# class OfficeBearerTypeForm(ModelForm):
#     class Meta:
#         model = GovernmentBodyType
#         fields = ['name', 'parent']

class OfficeBearerForm(ModelForm):
    class Meta:
        model = OfficeBearer
        fields = '__all__'
