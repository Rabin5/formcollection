from master_data.models import FiscalYear
from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.company import IsolationCenter
from master_data.models.government import GovernmentBody, Manpower


class IsolationManagementDetail(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, related_name='iso_management_body', verbose_name='निकायको नामः: ')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='iso_management_fiscal_year', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.body.name


class IsolationManagementDetailLine(FormLineBaseModel):
    isolationcenter = models.ForeignKey(
        IsolationCenter, on_delete=models.PROTECT, verbose_name='यस निकायले तयार वा सञ्चालन गरेको आईसोलेशन केन्द्रको नाम')
    cost_construction = models.FloatField(
        verbose_name='निर्माण खर्च ')
    num_bed = models.IntegerField(
        verbose_name='बेड संख्या')
    max_num_daily_stay = models.IntegerField(
        verbose_name='आईसोलेशन केन्द्रमा बस्नेहरुको दैनिकरुपमा बसेको अधिकतम  संख्या')
    num_stayed_till_fy_end = models.IntegerField(
        verbose_name='आईसोलेशन केन्द्रमा बस्नेहरुको आषाढ मसान्त सम्म आईसोलेशन केन्द्रमा बसेकाहरुको कुल संख्या')
    expense_operations = models.FloatField(
        verbose_name='ब्यबस्थापन प्रयोजनको खर्च')

    isolation_management_detail_line = models.ForeignKey(
        IsolationManagementDetail, on_delete=models.PROTECT, related_name='lines')
