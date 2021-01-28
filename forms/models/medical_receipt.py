from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, Product
from master_data.models.government import GovernmentBody
from master_data.models.address import Province, District
from master_data.models.company import Institution


class MedicalReceipt(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नाम')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='medical_receipt', verbose_name='आर्थिक बर्ष')

    def __str__(self):
        return self.body.name


class MedicalReceiptLine(FormLineBaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, verbose_name='स्वास्थ्य सामाग्री उपकरणको विवरण')
    provider_institution = models.ForeignKey(
        Institution, on_delete=models.PROTECT, related_name='institution_pro', verbose_name='प्रदान गर्ने संस्था')
    provider_body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, related_name='body_pro', verbose_name='प्रदान गर्ने निकाय')
    quantity = models.IntegerField(verbose_name='परिमाण')

    cost_received_items = models.FloatField(
        verbose_name='प्राप्त औषधी स्वास्थ्य सामग्री उपकरणको मूल्य')
    usage_situation = models.CharField(
        max_length=300, verbose_name='प्रयोगको अवस्था')
    medical_receipt_line = models.ForeignKey(
        MedicalReceipt, on_delete=models.PROTECT)
