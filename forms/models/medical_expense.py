from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import Product, FiscalYear, GovernmentBody, Importer, ProcurementMethod


class MedicalExpense(FormBaseModel):
    """
    Model for form class: 1_covid_hospital/3.puml
    Code: medExp
    """

    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, related_name='forms_medExp_fy', null=True, verbose_name='आर्थिक बर्ष: ')
    body = models.ForeignKey(GovernmentBody, on_delete=models.CASCADE, related_name="forms_medExp_gov", null=True, verbose_name='निकायको नामः: ')
    state = models.CharField(max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return self.fiscal_year.name


class MedicalExpenseLine(FormLineBaseModel):
    medical_expense = models.ForeignKey(
        MedicalExpense, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product', verbose_name="स्वास्थ्य सामाग्री उपकरण")
    importer = models.ForeignKey(Importer, on_delete=models.PROTECT, related_name='expenses', null=True, verbose_name='आपूर्तिकर्ताको नाम')
    procure_method = models.ForeignKey(ProcurementMethod, on_delete=models.PROTECT, related_name='expenses', null=True, verbose_name='खरिद विधि')
    amt_agreement = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="सम्झौता रकम ")
    date_to_import = models.CharField(max_length=15, blank=False, null=False, verbose_name='आपूर्ति गर्नुपर्ने मिति', default='01/01/2077')
    date_imported = models.CharField(max_length=15, blank=False, null=False, verbose_name='आपूर्ति गरेको मिति', default='01/01/2077')
    amt_imported = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='आपूर्ति भएको सामानको मुल्य')
    remarks = models.CharField(max_length=50, blank=True, null=True, verbose_name='कैफियत')
    
