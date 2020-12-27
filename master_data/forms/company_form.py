from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.company import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name',  'date_establishment']
