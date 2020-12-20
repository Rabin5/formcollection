import datetime

from django.db import models

import nepali_datetime


class FiscalYear(models.Model):
    ordering = ['start_date']
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=False)
    name = models.CharField(max_length=15, blank=False, null=False, verbose_name='आर्थिक वर्ष')
    date_start_bs = models.CharField(max_length=15, blank=False, null=False, verbose_name='सुरू मिति', default='01/01/2000')
    date_end_bs = models.CharField(max_length=15, blank=False, null=False, verbose_name='अन्त्य मिति', default='01/01/2000')

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
                (self.date_start <= fy.date_end) and \
                    (fy.date_start <= self.date_end)
                ):
                return False
        
        return True
