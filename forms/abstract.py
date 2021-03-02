from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class FormLineBaseModel(models.Model):
    created_date = models.DateField(
        verbose_name='सिर्जना मिति',
        auto_now_add=True
        )
    updated_date = models.DateField(
        verbose_name='अद्यावधिक मिति',
        auto_now=True
        )

    class Meta:
        abstract = True
        ordering = ['id']


class FormBaseModel(FormLineBaseModel):
    create_user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True
        ordering = ['id']
