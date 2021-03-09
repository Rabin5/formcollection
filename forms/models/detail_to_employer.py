from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.employer_type import EmployerType

class DetailToEmployer(FormBaseModel):
    pass


class DetailToEmployerLine(FormLineBaseModel):
    detail_to_emp_line = models.ForeignKey(
        DetailToEmployer, on_delete=models.CASCADE, related_name='lines')
    employer_name_address = models.CharField(max_length=250, verbose_name='रोजगारदाताको नाम ठेगाना ', blank=True, null=True)
    employer_type = models.ForeignKey(
        EmployerType, on_delete=models.CASCADE, verbose_name='रोजगारदाताको किसिम (सार्वजनिक आयोजन, निजी क्षेत्र, गैसस)')
    employer_notified_date = models.DateField(null=True, blank=False)
    


    def __str__(self):
        return str(self.employer_type.name)
