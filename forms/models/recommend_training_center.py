from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.training_center import TrainingCenter

class RecommendTrainingCenter(FormBaseModel):
    pass


class RecommendTrainingCenterLine(FormLineBaseModel):
    recommend_training_line = models.ForeignKey(
        RecommendTrainingCenter, on_delete=models.CASCADE, related_name='lines')
    training_subject = models.CharField(max_length=250, verbose_name='', blank=True, null=True)
    training_center = models.ForeignKey(
        TrainingCenter, on_delete=models.CASCADE, verbose_name='')
    num_employed = models.IntegerField(verbose_name='')
    employed_days = models.IntegerField(verbose_name='')


    def __str__(self):
        return str(self.employer_type.name)
