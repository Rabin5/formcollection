from forms.abstract import FormBaseModel, FormLineBaseModel
from django.db import models

# center footer 6.6 सेवा प्रवाह सम्बन्धी विवरण (स्थानीय तहको लागि)


class ServiceFlow(FormBaseModel):
    pass


class ServiceFlowLine(FormLineBaseModel):
    serice_flow = models.ForeignKey(
        ServiceFlow, on_delete=models.CASCADE, related_name='lines')
    description = models.CharField(max_length=100, verbose_name='विवरण')
    application_count = models.IntegerField(
        verbose_name='सेवा प्राप्ति को लागि  निबेदन संख्या ')
    recommendation_count = models.IntegerField(verbose_name='सिफारिस संख्या ')
    remarks = models.CharField(max_length=100, verbose_name='कैफेयत')

    def __str__(self):
        return self.description
