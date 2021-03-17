from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, GovernmentBody, OfficeBearer, AllowanceType
from master_data.models.training_center import TrainingCenter
# center footer 7.6 बेरोजगारहरुको ज्ञान, सीप, योग्यता, अनुभव र बजारको मागमा आधारमा आवश्यक पर्ने सीप विकास तालिमको पहिचान गरी सम्बन्धित तालिम केन्द्रमा सिफारिस गरेको विवरण


class RecommendTrainingCenter(FormBaseModel):
    pass


class RecommendTrainingCenterLine(FormLineBaseModel):
    ecommendtrainingcenter_line = models.ForeignKey(
        RecommendTrainingCenter, on_delete=models.CASCADE, null=True, blank=True, related_name='lines')
    training_subject = models.CharField(
        max_length=300, verbose_name='तालिमको विषय')
    training_center = models.ForeignKey(
        TrainingCenter, on_delete=models.CASCADE, verbose_name='तालिम केन्द्रको नाम')
    total_recommend = models.IntegerField(
        verbose_name='सिफारिस गरेको व्यक्ति संख्या')
    num_employed = models.IntegerField(
        verbose_name='रोजगारी प्राप्त गर्ने व्यक्ति संख्या')
    employed_days = models.IntegerField(verbose_name='रोजगारी प्राप्त दिन')

    def __str__(self):
        return str(self.training_subject)
