from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.company import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
