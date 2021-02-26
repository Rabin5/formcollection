from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import ProjectType


class StatePartnershipProgram(FormBaseModel):
    pass


class StatePartnershipProgramLine(FormLineBaseModel):
    project_type = models.ForeignKey(ProjectType,on_delete=models.PROTECT,blank=True, null=True,related_name='state_partnership_programs',verbose_name='आयोजनाको प्रकार')
    num_project = models.PositiveIntegerField(verbose_name='आयोजनाको संख्या')
    budget_amt = models.FloatField(verbose_name='बजेट रकम')
    spent_amount = models.FloatField(verbose_name='खर्च रकम')
    financial_progress_percentage = models.FloatField(verbose_name='वित्तीय प्रगति प्रतिशत')
    physical_progress_percentage = models.FloatField(verbose_name='भौतिक प्रगति प्रतिशत')
    state_partnership_program = models.ForeignKey(
        StatePartnershipProgram, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
