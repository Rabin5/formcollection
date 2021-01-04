from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES, BS_MONTHS
from master_data.models import Product
from .form_collection import FormCollection

class MedicalExpense(FormBaseModel):
    """
    Model for form class: 1_covid_hospital/3.puml
    Code: medExp
    """

    collection = models.ForeignKey(FormCollection, on_delete=models.CASCADE, related_name='collection', null=True)
    state = models.CharField(max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return f'{self.collection}'


class MedicalExpenseLine(FormLineBaseModel):
    medical_expense = models.ForeignKey(MedicalExpense, on_delete=models.CASCADE, related_name='lines')
    # TODO: relate procure_method, importer
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    # importer = models.ForeignKey(Importer, on_delete=models.PROTECT, related_name='importer')
    amt_agreement = models.DecimalField(max_digits=19, decimal_places=2)
    date_to_import = models.CharField(max_length=15, blank=False, null=False, verbose_name='आपूर्ति गर्नुपर्ने मिति', default='01/01/2000')
    date_imported = models.CharField(max_length=15, blank=False, null=False, verbose_name='आपूर्ति गरेको मिति', default='01/01/2000')
    amt_imported = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='आपूर्ति भएको सामानको मुल्य')
    remarks = models.CharField(max_length=50, blank=True, null=True, verbose_name='कैफियत')
    