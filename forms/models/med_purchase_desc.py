from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models import FiscalYear, GovernmentBody, \
    Product, UnitOfMeasure


class MedicalPurchaseDescription(FormBaseModel):
    """
    Model for form class: 1_covid_hospital/6.puml
    Code: med_purchase_desc
    """

    fiscal_year = models.ForeignKey(
        FiscalYear,
        on_delete=models.PROTECT,
        related_name='forms_medPurchase_fy',
        verbose_name='आर्थिक बर्ष'
        )
    body = models.ForeignKey(
        GovernmentBody,
        on_delete=models.CASCADE,
        related_name="forms_medPurchase_gov",
        verbose_name='निकायको नाम'
        )

    def __str__(self):
        return f'{self.body.name}'


class MedicalPurchaseDescriptionLine(FormLineBaseModel):
    medical_purchase = models.ForeignKey(
        MedicalPurchaseDescription,
        on_delete=models.CASCADE,
        related_name='lines'
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='सामानको नाम'
        )
    uom = models.ForeignKey(
        UnitOfMeasure,
        on_delete=models.CASCADE,
        verbose_name='इकाई'
        )
    product_specificaiton = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="सामानको छोटो स्पेशिफिकेशन"
        )
    date_procure_agreement = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        verbose_name='खरिद सम्झौता मिति',
        default='01/01/2077'
        )
    date_received = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        verbose_name='सामान प्राप्त मिति',
        default='01/01/2077'
        )
    qty = models.FloatField(blank=True, null=True, verbose_name='परीमाण')
    rate = models.FloatField(blank=True, null=True, verbose_name='दर')
    total_amt = models.FloatField(
        blank=True,
        null=True,
        verbose_name='कुल रकम'
        )
