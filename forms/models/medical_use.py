from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, Product
from master_data.models.government import GovernmentBody
from master_data.models.address import Province, District
from master_data.models.company import Institution


class MedicalUse(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नामः: ')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='medical_use', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.body.name


class MedicalUseLine(FormLineBaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, verbose_name='स्वास्थ्य सामाग्री उपकरणको विवरण')
    is_purchased = models.BooleanField(default=False, verbose_name='खरीद गरिएको ?')
    product_price = models.FloatField(verbose_name='सामानको मुल्य')
    unused_qty = models.IntegerField(verbose_name='प्रयोगमा नआएको परिमाण')
    unused_reason = models.CharField(
        max_length=300, verbose_name='प्रयोगमा नआएको कारण')
    remarks = models.CharField(max_length=300, verbose_name='कैफियत')
    medical_use_line = models.ForeignKey(
        MedicalUse, null=True, blank=True, on_delete=models.PROTECT)
