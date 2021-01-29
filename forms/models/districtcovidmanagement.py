from master_data.models import FiscalYear
from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.address import District
from master_data.models.government import GovernmentBody, Manpower


class DistrictCovidManagement(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, related_name='dist_quarantine_mgt_body', verbose_name='निकायको नामः: ')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='dist_quarantine_mgt_fiscal_year', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.body.name


class DisctrictQuarantineManagementLine(FormLineBaseModel):
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, related_name='dist_quarantine_mgt', verbose_name='जिल्ला')
    num_prepared_quarantine = models.IntegerField(
        verbose_name='तयार गरेको क्वारेन्टीन संख्या')
    num_prepared_quarantine_beds = models.IntegerField(
        verbose_name='तयार गरेको क्वारेन्टीन बेड संख्या')
    num_quarantined_person = models.IntegerField(
        verbose_name='क्वारेन्टीन बसेका व्यक्तिको संख्या')
    num_home_quarantined_person = models.IntegerField(
        verbose_name='होम क्वारेन्टिनमा बसेका व्यक्तिको संख्या')
    num_insufficient_bed = models.IntegerField(
        verbose_name='नपुग वेड संख्या')
    quarantine_mgmgt_lines = models.ForeignKey(
        DistrictCovidManagement, on_delete=models.PROTECT)


class DistrictIsolationManagementLine(FormLineBaseModel):
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, related_name='dist_isolation_mgt', verbose_name='जिल्ला')
    num_prepared_icu = models.IntegerField(
        verbose_name='तयारी अवस्थामा रहेको icu  संख्या')
    num_prepared_bed = models.IntegerField(
        verbose_name='तयारी अवस्थामा रहेको बेड संख्या')
    num_infected_person = models.IntegerField(
        verbose_name='संक्रमित संख्या')
    num_isolated_person = models.IntegerField(
        verbose_name='आईसोलेशनमा बस्नेको संख्या')
    num_home_isolated_person = models.IntegerField(
        verbose_name='होम आईसोलेशनमा बस्नेको संख्या')
    isolation_mgmt_lines = models.ForeignKey(
        DistrictCovidManagement, on_delete=models.PROTECT)


class DistrictLabTestLine(FormLineBaseModel):
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, related_name='dist_labtest_mgt', verbose_name='जिल्ला')
    num_rdt_tests = models.IntegerField(
        verbose_name='आरडीटी परीक्षण')
    num_rdt_results_received = models.IntegerField(
        verbose_name='आरडीटी नतिजा प्राप्त')
    num_rdt_positive_results = models.IntegerField(
        verbose_name='आरडीटी पोजेटिभ नतिजा')
    num_pcr_tests = models.IntegerField(
        verbose_name='पीसीआर परीक्षण')
    num_pcr_results_received = models.IntegerField(
        verbose_name='पीसीआर नतिजा प्राप्त')
    num_pcr_positive_results = models.IntegerField(
        verbose_name='पीसीआर पोजेटिभ नतिजा')
    num_pcr_contract_trace = models.IntegerField(
        verbose_name='पीसीआर परीक्षण मध्ये कन्ट्रयाक ट्रेसिङ्गको आधारमा गरेको परीक्षण')
    num_covid_treated_patients = models.IntegerField(
        verbose_name='उपचार गराएका कोरोना विरामी संख्या')
    num_covid_recovered_patients = models.IntegerField(
        verbose_name='उपचार पछि निको भई घर गएको संख्या')
    num_isolation_treatments = models.IntegerField(
        verbose_name='आइसोलेसनमा उपचार गराउने संख्या')
    num_icu_treatments = models.IntegerField(
        verbose_name='आई सी यु मा उपचार गराउने संख्या')
    num_covid_deaths = models.IntegerField(
        verbose_name='मृत्यु हुनेको संख्या')
    lab_test_lines = models.ForeignKey(
        DistrictCovidManagement, on_delete=models.PROTECT)
