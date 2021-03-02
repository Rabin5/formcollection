from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, GovernmentBody, OfficeBearer, AllowanceType
from master_data.models.school import School


class TeacherDesignation(FormBaseModel):
    pass


class TeacherDesignationLine(FormLineBaseModel):
    teacherdesignation_line = models.ForeignKey(
        TeacherDesignation, on_delete=models.CASCADE, related_name='lines')
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='lines', verbose_name='विधालयको नाम')
    num_vacancy = models.IntegerField(verbose_name='शिक्षक दरबन्दी')
    num_vacancy_filled = models.IntegerField(verbose_name='पदपूर्ति')
    num_temp_filled = models.IntegerField(verbose_name='पदपूर्ति मध्ये करार')
    num_student = models.IntegerField(verbose_name='विधार्थी संख्या')

    def __str__(self):
        return str(self.school.name)
