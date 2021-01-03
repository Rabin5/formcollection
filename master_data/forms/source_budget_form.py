from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.government import SourceBudget


# class OfficeBearerTypeForm(ModelForm):
#     class Meta:
#         model = GovernmentBodyType
#         fields = ['name', 'parent']

class SourceBudgetForm(ModelForm):
    class Meta:
        model = SourceBudget
        fields = '__all__'
