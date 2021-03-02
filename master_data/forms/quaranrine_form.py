from django.core.exceptions import ValidationError
from django.forms import ModelForm
from master_data.models.company import QuanrantineCenter


class QuanrantineCenterForm(ModelForm):
    class Meta:
        model = QuanrantineCenter
        fields = (
            'name', 'country', 'province', 'district', 'local_level', 'ward',
        )
