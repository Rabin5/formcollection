from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import ProjectType


class LocalPartnershipProgram(FormBaseModel):
    pass


class LocalPartnershipProgramLine(FormLineBaseModel):
    project_name = models.CharField(max_length=300, blank=True, null=True, verbose_name='आयोजनाको नाम')
    project_type=models.ForeignKey(ProjectType,on_delete=models.PROTECT,related_name='local_partnership_programs',verbose_name='आयोजनाको प्रकार')
    cost_estimation = models.FloatField(verbose_name='लागत अनुमान')
    programme_amount = models.FloatField(verbose_name='कार्यक्रमबाट')
    local_level_amount = models.FloatField(verbose_name='स्थानीय तहबाट')
    other_amount = models.FloatField(verbose_name='गैसस वा अन्य')
    public_participation_amount = models.FloatField(verbose_name='लागत सहभागितबाट व्यहोरिने रकम')
    total_amount = models.FloatField(verbose_name='जम्मा')
    project_completed_amount = models.FloatField(blank=True, null=True, verbose_name='कार्य सम्पन्न रकम')
    concerned_member_name= models.CharField(max_length=300,verbose_name='सम्बन्धीत सभासदको नाम')
    local_partnership_program = models.ForeignKey(
         LocalPartnershipProgram, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
