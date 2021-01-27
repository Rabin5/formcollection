from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models import GovernmentBody, ActionPlanActivity
from collection.utils import STATES


class ActionPlanImplementation(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नामः')
    state = models.CharField(
        max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return self.body.name


class ActionPlanImplementationLine(FormLineBaseModel):
    action_plan_implementation = models.ForeignKey(
        ActionPlanImplementation, on_delete=models.PROTECT, verbose_name='कार्य योजना कार्यान्वयन')
    activity = models.ForeignKey(
        ActionPlanActivity, on_delete=models.PROTECT, verbose_name='क्रियाकलाप')
    work_done = models.CharField(max_length=500, verbose_name='प्रदेश सरकारबाट भएको कार्य')
    work_expense = models.FloatField(verbose_name='उक्त कार्यमा भएको खर्च')

    def __str__(self):
        return self.action_plan_implementation.body.name
