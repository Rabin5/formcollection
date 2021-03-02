from forms.abstract import FormBaseModel, FormLineBaseModel
from django.db import models
from master_data.models import GovernmentBody
from master_data.modesls.vehicle import Vechile
# 8. सवारी साधन खरिदको विवरण (स्थानीय तहको लागि)
center footer 6.8 सवारी साधन खरिदको विवरण(स्थानीय तहको लागि)


class VehiclePurchase(FormBaseModel):
    pass


class VehiclePurchaseLine(FormLineBaseModel):
    vehiclepurchase_line = models.ForeignKey(
        VehiclePurchase, on_delete=models.CASCADE, related_name='lines')
    vehicle = models.ForeignKey(
        Vechile, on_delete=models.CASCADE, verbose_name='सवारी साधन')
    purchased_amount = models.IntegerField(verbose_name='खरिद संख्या')
    price = models.FloatField(verbose_name='मूल्य')
    body = models.ForeignKey(
        Body, on_delete=models.CASCADE, verbose_name='विप्रयोग गर्नेपदाधिकारी र्सस्थावरण')
    remarks = models.CharField(max_length=300, verbose_name='कैफियत')

    def __str__(self):
        return self.vehicle
