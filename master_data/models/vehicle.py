from django.db import models


class Vehicle(models.Model):
    ordering = ['start_date']
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='सवारी साधन')

    def __str__(self):
        return str(self.name)
