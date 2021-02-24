
from master_data.models import FiscalYear
from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel

# ' 7. घर नक्शापास र निर्माण कार्य सम्पन्न सम्बन्धी विवरण (स्थानीय तहको लागि)
# center footer 6.7 घर नक्शापास र निर्माण कार्य सम्पन्न सम्बन्धी विवरण (स्थानीय तहको लागि)


class HouseMapConstruction(FormBaseModel):
    pass


class HouseMapConstructionLine(FormLineBaseModel):
    housemapconstruction_line = models.ForeignKey(
        HouseMapConstruction, on_delete=models.CASCADE, related_name='lines')
    application_count = models.IntegerField(
        verbose_name='घरनक्शा पासको निवेदन संख्या')
    temporary_permission = models.BooleanField(
        default=False, verbose_name='अस्थायी अनुमति')
    prev_year_approved_num = models.IntegerField(
        verbose_name='कार्यसम्पन्न संख्या गत विगत वर्ष अनुमति लिएका मध्ये')
    current_year_approved_num = models.IntegerField(
        verbose_name='कार्यसम्पन्न संख्या यो वर्ष अनुमति लिएका मध्ये')
    total = models.IntegerField(verbose_name='जम्मा')
    remarks = models.CharField(max_length=300, verbose_name='कैफियत')

    def __str__(self):
        return self.application_count
