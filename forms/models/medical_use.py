from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, Product
from master_data.models.government import GovernmentBody
from master_data.models.address import Province, District
from master_data.models.company import Institution


class MedicalUse(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नाम')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='medical_use', verbose_name='आर्थिक बर्ष')

    def __str__(self):
        return self.body.name


class MedicalUseLine(FormLineBaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, verbose_name='औषधी स्वास्थ्य सामग्री एवं उपकरणको नाम')
    is_purchased = models.BooleanField(default=False, verbose_name='खरिद वा प्राप्ती? यदि खरीद गरिएको भए टिक गर्नुहोस्')
    product_price = models.FloatField(verbose_name='सामानको मुल्य')
    unused_qty = models.IntegerField(verbose_name='प्रयोगमा नआएको परिमाण')
    unused_reason = models.CharField(
        max_length=300, verbose_name='प्रयोगमा नआएको कारण')
    remarks = models.CharField(max_length=300, verbose_name='कैफियत')
    medical_use_line = models.ForeignKey(
        MedicalUse, related_name='medical_use_lines', null=True, blank=True, on_delete=models.PROTECT)
