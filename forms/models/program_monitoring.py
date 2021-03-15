from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, GovernmentBody


class ProgramMonitoring(FormBaseModel):
    pass


class ProgramMonitoringLine(FormLineBaseModel):
    fiscal_year=models.ForeignKey(FiscalYear, verbose_name='आर्थिक बर्ष', on_delete=models.PROTECT)
    program_name = models.CharField(verbose_name='आयोजनाको नाम', max_length=255)
    follow_up_date = models.DateField(verbose_name='अनुगमन मित')
    monitoring_body=models.ForeignKey(GovernmentBody, verbose_name='अनुगमन गर्ने निकाय/ संयन्त्र', on_delete=models.PROTECT)
    behaviour = models.TextField(verbose_name='बैठकको निर्णयहरु')
    
    program_monitoring_line = models.ForeignKey(
        ProgramMonitoring, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
