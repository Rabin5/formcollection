from django.db import models

class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name='नाम')

    def __str__(self) -> str:
        return self.name

class ProcurementMethod(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name='नाम')

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    ordering = ['start_date']
    created = models.DateTimeField(auto_now_add=True)
    # date_end = models.DateTimeField(null=False, auto_now=True)
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='नाम')
    description = models.TextField(blank=True, verbose_name='वर्णन')
    type = models.CharField(max_length=255, blank=False, null=False, verbose_name='प्रकार')
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, blank=True, null=True, verbose_name='मापनको एकाई')


    def __str__(self) -> str:
        return self.name
    
