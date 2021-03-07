from django.forms import ModelForm

from master_data.models.training_center import *


class TrainingCenterForm(ModelForm):
    class Meta:
        model = TrainingCenter
        fields = ['name', ]
     