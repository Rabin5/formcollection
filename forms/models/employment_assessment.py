from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.fiscal_year import FiscalYear

class EmploymentAssessment(FormBaseModel):
    pass


class EmploymentAssessmentLine(FormLineBaseModel):
    emp_assessment_line = models.ForeignKey(
        EmploymentAssessment, on_delete=models.CASCADE, related_name='lines')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.CASCADE, verbose_name='आर्थिक बर्ष')
    available_employment = models.IntegerField(verbose_name='उपलव्ध हुन सक्ने रोजगारीको (संख्यामा)')
    employment_sector = models.CharField(max_length=250, verbose_name='रोजगारीका सम्भावित क्षेत्रहरु', blank=True, null=True)


    def __str__(self):
        return str(self.fiscal_year.name)
