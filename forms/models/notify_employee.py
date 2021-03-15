from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.employer_type import EmployerType

class NotifyEmployee(FormBaseModel):
    pass


class NotifyEmployeeLine(FormLineBaseModel):
    notify_employee_line = models.ForeignKey(
        NotifyEmployee, on_delete=models.CASCADE, related_name='lines')
    employer_name_address = models.CharField(max_length=250, verbose_name='रोजगारदाताको नाम ठेगाना ', blank=True, null=True)
    employer_type = models.ForeignKey(
        EmployerType, on_delete=models.CASCADE, verbose_name='रोजगारदाताको किसिम (सार्वजनिक आयोजन, निजी क्षेत्र, गैसस)')
    num_workers_provided = models.IntegerField(verbose_name='उपलव्ध गराएको श्रमिक संख्या ')
    employment_provided_total_days = models.IntegerField(verbose_name='जम्मा दिन')
    employment_provided_days_per_person = models.IntegerField(verbose_name='प्रतिव्यक्ति दिन ')


    def __str__(self):
        return str(self.employer_type.name)
