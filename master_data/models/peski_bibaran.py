from django.db import models
from django.db.models.fields import TextField

class PeskiBibaran(models.Model):
    ordering = ['start_date']
    created = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(blank=False, null=False, verbose_name='नाम')
        
    # def __str__(self) -> str:
    #     return self.name
