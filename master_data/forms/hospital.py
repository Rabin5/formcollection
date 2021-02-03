from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm
from master_data.widgets import NepaliDateInput
import nepali_datetime

from master_data.models.hospital import *


class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', ]
    
class CovidHospitalForm(HospitalForm):
    def __init__(self, *args, **kwargs):
        super(CovidHospitalForm, self).__init__(*args,**kwargs)

    class Meta(HospitalForm.Meta):
        model = CovidHospital
        # fields = ['type', 'date_announcement']
        fields = HospitalForm.Meta.fields + ['type', 'date_announcement', 'province', 'district', 'local_level']
        widgets = {
            'date_announcement': NepaliDateInput(),
        }

    def save(self, commit=True):
        covDate = super().save(commit=False)
        covDate.date_start = nepali_datetime.datetime.strptime(covDate.date_announcement, '%d/%m/%Y').date().to_datetime_date()
        covDate.save()
        return covDate