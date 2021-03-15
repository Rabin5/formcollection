from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.fiscal_year import FiscalYear

class RegisteredUnemployment(FormBaseModel):
    pass


class RegisteredUnemploymentLine(FormLineBaseModel):
    reg_unemployment_line = models.ForeignKey(
        RegisteredUnemployment, on_delete=models.CASCADE, related_name='lines')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.CASCADE, verbose_name='आर्थिक बर्ष')
    unemployed_registered_num = models.IntegerField(verbose_name='दर्ता गरिएका बेरोजगार संख्या')
    employed_registered_num = models.IntegerField(verbose_name='दर्ता भएको मध्येबाट रोजगारी प्रधान गरीएको संख्या ')
    employment_provided_total_days = models.IntegerField(verbose_name='जम्मा दिन')
    employment_provided_days_per_person = models.IntegerField(verbose_name='प्रति व्यक्ति दिन')
    

    def __str__(self):
        return str(self.fiscal_year.name)
