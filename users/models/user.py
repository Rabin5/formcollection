from django.contrib.auth.models import AbstractUser
from django.db import models

# from master_data.models import GovernmentBody


class User(AbstractUser):
    # body = models.ForeignKey(GovernmentBody, on_delete=models.RESTRICT, related_name='users', verbose_name='निकाय')
    mobile_number = models.CharField(max_length=10, verbose_name='मोबाइल नम्बर', null=True, blank=True)