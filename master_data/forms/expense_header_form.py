from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.government import ExpenseHeader


# class OfficeBearerTypeForm(ModelForm):
#     class Meta:
#         model = GovernmentBodyType
#         fields = ['name', 'parent']

class ExpenseHeaderForm(ModelForm):
    class Meta:
        model = ExpenseHeader
        fields = '__all__'
