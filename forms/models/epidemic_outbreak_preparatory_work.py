from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models import FiscalYear, GovernmentBody
from forms.utils import STATES


class EpidemicOutbreakPreparatoryWork(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नामः:')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='epidemic_outbreak_preparatory_work', verbose_name='आर्थिक बर्ष: ')
    state = models.CharField(
        max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return self.body.name


class EpidemicOutbreakPreparatoryWorkLine(FormLineBaseModel):
    epidemic_outbreak_preparatory_work = models.ForeignKey(
        EpidemicOutbreakPreparatoryWork, on_delete=models.PROTECT, verbose_name='महामारीको प्रकोप तयारी कार्य')
    preparation_work_to_do = models.CharField(
        max_length=500, verbose_name='पूर्व तयारी सम्बन्धी गर्नुपर्ने कार्य')
    major_activities = models.CharField(
        max_length=500, verbose_name='सम्पादन भएका प्रमुख क्रियाकलापहरु')
    amt_expense = models.FloatField(verbose_name='खर्च रकम')

    def __str__(self):
        return self.epidemic_outbreak_preparatory_work.body.name
