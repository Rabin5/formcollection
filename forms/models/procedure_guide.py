from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS


class ProcedureGuide(FormBaseModel):
    pass


class ProcedureGuideLine(FormLineBaseModel):
    desc = models.TextField(verbose_name='विवरण')
    act =models.CharField(max_length=300,verbose_name='ऐन ')
    rules =models.CharField(max_length=300,verbose_name='नियमावली')
    procedure_desc = models.CharField(max_length=300,verbose_name='कार्यविधि')
    directory =models.CharField(max_length=300,verbose_name='निर्देशिका')
    norms =models.CharField(max_length=300,verbose_name='नर्म्स')
    total = models.FloatField(verbose_name='जम्मा')
    procedure_guide = models.ForeignKey(
        ProcedureGuide, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')