from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES
from master_data.models import CovidHospital, Product


class CovidHospitalEquipment(FormBaseModel):
    """
    Model for form class: 1_covid_hospital/12.puml
    """

    cov_hospital = models.ForeignKey(CovidHospital, on_delete=models.CASCADE, related_name='forms_cov_hos')

    def __str__(self):
        return f'{self.cov_hospital}'


class CovidHospitalEquipmentLine(FormLineBaseModel):
    cov_hos_equip = models.ForeignKey(CovidHospitalEquipment, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='स्वास्थ्य उपकरण')
    num_required = models.IntegerField(blank=True, null=True, verbose_name='आबश्यक')
    available = models.IntegerField(blank=True, null=True, verbose_name='उपलब्ध')
    num_still_required = models.IntegerField(blank=True, null=True, verbose_name='नपुग')
    