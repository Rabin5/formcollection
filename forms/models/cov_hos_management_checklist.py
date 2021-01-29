from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES
from master_data.models import CovidHospital, CovidHospitalManagementChecklistDescription


class CovidHospitalManagementChecklist(FormBaseModel):
    """
    Model for form class: 1_covid_hospital/18.puml
    """
    hospital = models.ForeignKey(CovidHospital, on_delete=models.PROTECT, null=True, verbose_name='अस्पतालको नामः: ')
    state = models.CharField(max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return f'{self.hospital.name}'


class CovidHospitalManagementChecklistLine(FormLineBaseModel):
    cov_hos_management = models.ForeignKey(CovidHospitalManagementChecklist, on_delete=models.CASCADE, related_name='lines', blank=True, null=True)
    description = models.ForeignKey(CovidHospitalManagementChecklistDescription, on_delete=models.CASCADE, verbose_name='बिबरण')
    is_yes = models.BooleanField(default=False, verbose_name='छ')
    # is_no = models.BooleanField(default=False, verbose_name='छैन')
    remarks = models.CharField(max_length=50, blank=True, null=True, verbose_name='कैफियत')

    def __str__(self):
        return self.description.description
    
    