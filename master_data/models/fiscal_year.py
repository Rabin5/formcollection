import datetime

from django.db import models

import nepali_datetime


class FyQuerySet(models.QuerySet):
    def current_fy(self):
        for fy in self:
            if fy.is_current:
                return fy


class FyManager(models.Manager):
    def get_current_fy(self):
        return self.get_queryset().current_fy()


class FiscalYear(models.Model):
    ordering = ['start_date']
    objects = FyManager.from_queryset(FyQuerySet)()
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=False)
    name = models.CharField(max_length=200, blank=False,
                            null=False, verbose_name='आर्थिक वर्ष')
    date_start_bs = models.CharField(
        max_length=15, blank=False, null=False, verbose_name='सुरू मिति', default='01/01/2000')
    date_end_bs = models.CharField(
        max_length=15, blank=False, null=False, verbose_name='अन्त्य मिति', default='01/01/2000')

    @property
    def is_current(self):
        if self.date_start <= datetime.date.today() <= self.date_end:
            return True
        return False

    def __str__(self):
        return self.name

    def is_unique(self):
        if (self.date_start >= self.date_end):
            return False

        fys = FiscalYear.objects.all()

        for fy in fys:
            if (
                    (self.date_start <= fy.date_end) and
                (fy.date_start <= self.date_end)
            ):
                return False

        return True


def get_current_fy():
    return FiscalYear.objects.get_current_fy().id