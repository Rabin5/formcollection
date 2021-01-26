from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES
from master_data.models import FiscalYear, GovernmentBody, \
    Laboratory


class PcrKitUsage(FormBaseModel):
    """
    Model for form class: 1_covid_hospital/10.puml
    """

    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, related_name='forms_pcrKit_fy', verbose_name='आर्थिक बर्ष: ')
    body = models.ForeignKey(GovernmentBody, on_delete=models.CASCADE, related_name="forms_pcrKit_gov", verbose_name='निकायको नामः: ')

    def __str__(self):
        return f'{self.body.name}'


class PcrKitUsageLine(FormLineBaseModel):
    pcr_kit_usage = models.ForeignKey(PcrKitUsage, on_delete=models.CASCADE, related_name='lines')
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE, verbose_name='प्रयोगशालाको नाम')
    num_kit_received = models.IntegerField(blank=True, null=True, verbose_name='२०७६ चैत्र देखि २०७७ आषाढ सम्म पिसीआर किट प्राप्ती')
    num_kit_expensed = models.IntegerField(blank=True, null=True, verbose_name='२०७७ आषाढमसान्त सम्म पीसिआर किट खर्च')
    num_kit_available = models.IntegerField(blank=True, null=True, verbose_name='२०७७ आषाढमसान्त मौजदात किट')
    num_tests = models.IntegerField(blank=True, null=True, verbose_name='परीक्षण संख्या')
    num_wasted = models.IntegerField(blank=True, null=True, verbose_name='वेष्टेज गएको किट संख्या')
    