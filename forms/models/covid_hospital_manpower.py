from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.hospital import CovidHospital
from master_data.models.government import Manpower


class CovidHospitalManpower(FormBaseModel):
    covidhospital = models.ForeignKey(
        CovidHospital,
        on_delete=models.PROTECT,
        verbose_name='कोभिड डेडिकेटेड अस्पातालको नाम',
        null=True,
        blank=True
    )

    def __str__(self):
        if self.covidhospital:
            return self.covidhospital.name
        return ""


class CovidHospitalManpowerLine(FormLineBaseModel):
    manpower = models.ForeignKey(
        Manpower, on_delete=models.PROTECT, verbose_name='स्वास्थ्य जनशक्ति')
    num_required = models.IntegerField(verbose_name='दरबन्दी संख्या')
    num_hired = models.IntegerField(verbose_name='पदपूर्ति संख्या')
    num_vacant = models.IntegerField(verbose_name='रिक्त संख्या')

    num_contract = models.IntegerField(
        verbose_name='पदपूर्ति मध्ये करार संख्या')
    covidhospital_manpower_line = models.ForeignKey(
        CovidHospitalManpower, on_delete=models.PROTECT, related_name='lines')
