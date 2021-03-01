from django.db import models

class ConvenienceType(models.Model):
    ordering = ['start_date']
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='सुविधाको किसिम')
    
    def __str__(self) -> str:
        return self.name
