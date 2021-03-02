from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import Designation
from master_data.models import Country



class ForeignTrip(FormBaseModel):
    pass


class ForeignTripLine(FormLineBaseModel):
    name =models.CharField(max_length=300,verbose_name='बैदेशिक भ्रमणमा जानेको पद र नाम ')
    designation =models.ForeignKey(Designation,on_delete=models.PROTECT,verbose_name='',null=True,blank=True)
    country =models.ForeignKey(Country,on_delete=models.PROTECT,verbose_name='भ्रमण गरेको देश',related_name='foreign_trip_line')
    payment_amount=models.FloatField(verbose_name='भुक्तानी रकम')
    foreign_trip = models.ForeignKey(
        ForeignTrip, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')