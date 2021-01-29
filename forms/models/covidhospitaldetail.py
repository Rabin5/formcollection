from master_data.models import FiscalYear
from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.hospital import CovidHospital
from master_data.models.government import GovernmentBody, Manpower


class CovidHospitalDetail(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, related_name='covid_hospital_details', verbose_name='निकायको नामः: ')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='covid_hospital_fiscal_year', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.body.name


class CovidHospitalDetailLine(FormLineBaseModel):
    covidhospital = models.ForeignKey(
        CovidHospital, on_delete=models.PROTECT, verbose_name='डेडिकेटेड अस्पतालको नाम र स्थान')
    date_announcement = models.DateField(null=True, blank=False)
    announce_time_health_workers = models.IntegerField(
        verbose_name='कोभिड अस्पताल घोषणा हुँदाको अवस्थामा रहेको स्वास्थ्यकर्मीको संख्या')
    announce_time_beds = models.IntegerField(
        verbose_name='कोभिड अस्पताल घोषणा हुँदाको अवस्थामा रहेको बेड संख्या')
    announce_time_icu = models.IntegerField(
        verbose_name='कोभिड अस्पताल घोषणा हुँदाको अवस्थामा रहेको आई सी यु संख्या')
    announce_time_ventilators = models.IntegerField(
        verbose_name='कोभिड अस्पताल घोषणा हुँदाको अवस्थामा रहेको भेन्टिलेटर संख्या')
    added_health_workers = models.IntegerField(
        verbose_name='२०७७ असार मसान्तसम्म थप भएको स्वास्थ्यकर्मीको संख्या')
    added_beds = models.IntegerField(
        verbose_name='२०७७ असार मसान्तसम्म थप भएको बेड संख्या')
    added_icu = models.IntegerField(
        verbose_name='२०७७ असार मसान्तसम्म थप भएको आई सी यु संख्या')
    added_ventilators = models.IntegerField(
        verbose_name='२०७७ असार मसान्तसम्म थप भएको भेन्टिलेटर संख्या')
    num_treated_patients = models.IntegerField(
        verbose_name='२०७७ असार मसान्तसम्म उपचार गरेको कोभिड विरामी संख्या')
    expense_treatment = models.FloatField(
        verbose_name='२०७७ असार मसान्तसम्म उपचारमा भएको खर्च')
    covidhospital_hospital_detail_line = models.ForeignKey(
        CovidHospitalDetail, on_delete=models.PROTECT)
