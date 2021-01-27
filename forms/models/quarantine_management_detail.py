from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES
from master_data.models import IsolationCenter, FiscalYear, GovernmentBody


class QuarantineManagementDetail(FormBaseModel):
    """
    Model for form class: 1_covid_hospital/14.puml
    Code: medExp
    """
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, related_name='forms_quarantine_fy', null=True, verbose_name='आर्थिक बर्ष: ')
    body = models.ForeignKey(GovernmentBody, on_delete=models.CASCADE, related_name="forms_quarantine_gov", null=True, verbose_name='निकायको नामः: ')
    state = models.CharField(max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return f'{self.fiscal_year}'


class QuarantineManagementDetailLine(FormLineBaseModel):
    quarantine_management = models.ForeignKey(QuarantineManagementDetail, on_delete=models.CASCADE, related_name='lines')
    isolation_center = models.ForeignKey(IsolationCenter, on_delete=models.CASCADE, related_name='isolation_center', verbose_name='यस निकायले तयार वा सञ्चालन गरेको क्वारेन्टिन/होल्डिङ सेन्टरको नाम')
    cost_construction = models.FloatField( verbose_name='निर्माण खर्च')
    num_bed = models.IntegerField(verbose_name='बेड संख्या')
    max_num_daily_stay = models.IntegerField(verbose_name='दैनिकरुपमा बसेको अधिकतम  संख्या')
    num_stayed_till_fy_end = models.IntegerField(verbose_name='आषाढ मसान्त सम्म क्वारेन्टिनमा बसेकाहरुको कुल संख्या')
    expense_operations = models.FloatField( verbose_name='सञ्चालन ब्यबस्थापन प्रयोजनको खर्च')

    