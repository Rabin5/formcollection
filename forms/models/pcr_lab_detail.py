from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, GovernmentBody, \
    Laboratory

class PcrLaboratoryDetail(FormBaseModel):
    """
    Model for form class: 1_covid_hospital/8.puml
    """

    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, related_name='forms_pcr_lab_fy', verbose_name='आर्थिक बर्ष: ')
    body = models.ForeignKey(GovernmentBody, on_delete=models.CASCADE, related_name="forms_pcr_lab_gov", verbose_name='निकायको नामः: ')

    def __str__(self):
        return f'{self.body.name}'


class PcrLaboratoryDetailLine(FormLineBaseModel):
    pcr_lab_detail = models.ForeignKey(PcrLaboratoryDetail, on_delete=models.CASCADE, related_name='lines')
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE, verbose_name='पीसीआर ल्यावको नाम र स्थान')
    num_tested_fy_end = models.IntegerField(blank=True, null=True, verbose_name="आषाढ मसान्तसम्म परीक्षण गरेको कुल संख्या")
    num_infected = models.IntegerField(blank=True, null=True, verbose_name='परीक्षण मध्ये संक्रमितको संख्या')
    time_test_result = models.FloatField(blank=True, null=True, verbose_name='नतिजा दिन लाग्ने औषत समय')
    expense_pcr_test = models.FloatField(blank=True, null=True, verbose_name='पीसीआर परीक्षणमा आषाढ समान्त सम्म भएको खर्च')
    