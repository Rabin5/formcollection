from django.db import models

class ComplaintType(models.Model):
    ordering = ['start_date']
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='उजुरीको प्रकार')
    
    def __str__(self) -> str:
        return self.name
