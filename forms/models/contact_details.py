from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS


class ContactDetails(FormBaseModel):
    pass


class ContactDetailsLine(FormLineBaseModel):
    designation = models.CharField(verbose_name='पद', max_length=255)
    name = models.CharField(verbose_name='नाम', max_length=255)
    contact_number = models.IntegerField(verbose_name='सम्पर्क नम्बर')
    email = models.CharField(verbose_name='सम्पर्क इमेल ', max_length=255)
    
    contact_details_line = models.ForeignKey(
        ContactDetails, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
