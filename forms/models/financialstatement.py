from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
import nepali_datetime
import datetime


class FinancialStatement(FormBaseModel):
    pass


class FinancialStatementResponsibilityLine(FormLineBaseModel):
    financialstatement_line = models.ForeignKey(
        FinancialStatement, on_delete=models.CASCADE, related_name='lines_res')
    desc = models.CharField(max_length=300, verbose_name='विवरण')
    is_true = models.BooleanField(default=False, verbose_name='छ वा छैन')
    deadline = models.DateField(
        null=True, blank=False, verbose_name='गतको बर्षको अन्तिम मौदात')
    start_date = models.DateField(
        null=True, blank=False, verbose_name='यस बर्षको सुरु मौदात')
    increased_responsibility = models.CharField(
        max_length=300, verbose_name='निर्माण कार्यमा भएको कुल खर्च')
    num_insufficient_bed = models.IntegerField(
        verbose_name='घटि वढि जिम्मेवारी')
    way_of_looking = models.CharField(
        max_length=300, verbose_name='हेर्ने तरिका')

    def __str__(self):
        return str(self.desc)


class FinancialStatementBankAccountReconciledLine(FormLineBaseModel):
    financialstatement_line = models.ForeignKey(
        FinancialStatement, on_delete=models.CASCADE, related_name='lines_bankac')
    desc = models.CharField(max_length=300, verbose_name='विवरण')
    is_true = models.BooleanField(default=False, verbose_name='छ वा छैन')
    remaining_per_account = models.FloatField(
        verbose_name='खाता अनुसारको बाँकी')
    remaining_per_bank = models.FloatField(
        verbose_name='बैंक अनुसार बाँकी')
    difference = models.FloatField(
        verbose_name='फरक')
    way_of_looking = models.CharField(
        max_length=300, verbose_name='हेर्ने तरिका')

    def __str__(self):
        return str(self.desc)


class FinancialStatementDeductAmountLine(FormLineBaseModel):
    financialstatement_line = models.ForeignKey(
        FinancialStatement, on_delete=models.CASCADE, related_name='lines_finalst')
    desc = models.CharField(max_length=300, verbose_name='विवरण')
    amount = models.FloatField(verbose_name='रकम')
    way_of_looking = models.CharField(
        max_length=300, verbose_name='हेर्ने तरिका')

    def __str__(self):
        return str(self.desc)


class GrantReturnLine(FormLineBaseModel):
    financialstatement_line = models.ForeignKey(
        FinancialStatement, on_delete=models.CASCADE, related_name='lines_grant')
    desc = models.CharField(max_length=300, verbose_name='विवरण')
    is_true = models.BooleanField(default=False, verbose_name='छ वा छैन')
    remaining_per_federal_government = models.FloatField(
        verbose_name='संघीय सरकारतर्फको बाँकी')
    remaining_per_state_government = models.FloatField(
        verbose_name='प्रदेश सरकारतर्फको बाँकी')
    remaining = models.FloatField(verbose_name='जम्मा फिर्ता गर्न बाँकी')
    way_of_looking = models.CharField(
        max_length=300, verbose_name='हेर्ने तरिका')

    def __str__(self):
        return str(self.desc)


class RevenueDistributedLine(FormLineBaseModel):
    financialstatement_line = models.ForeignKey(
        FinancialStatement, on_delete=models.CASCADE, related_name='lines_renenu')
    desc = models.CharField(max_length=300, verbose_name='विवरण')
    is_true = models.BooleanField(default=False, verbose_name='छ वा छैन')
    remaining_distribution = models.FloatField(
        verbose_name='बाँडफाँड गर्न बाँकी रकम')
    remaining_amount_federal_gov = models.FloatField(
        verbose_name='संघीय सरकारलाई पठाउन बाँकी रकम')
    remaining_amount_state_gov = models.FloatField(
        verbose_name='प्रदेश सरकारलाई पठाउन बाँकी रकम')
    way_of_looking = models.CharField(
        max_length=300, verbose_name='हेर्ने तरिका')

    def __str__(self):
        return str(self.desc)


class RemainingAdvanceLine(FormLineBaseModel):
    financialstatement_line = models.ForeignKey(
        FinancialStatement,  on_delete=models.CASCADE, related_name='lines_ad')
    remaining_advance = models.CharField(
        max_length=300, verbose_name='५ पेश्की बाँकी ')
    not_expired = models.CharField(
        max_length=300, verbose_name='म्याद ननाघेको')
    expired = models.CharField(max_length=300, verbose_name='म्याद नाघेको')
    total = models.FloatField(verbose_name='जम्मा')
    way_of_looking = models.CharField(
        max_length=300, verbose_name='हेर्ने तरिका')

    def __str__(self):
        return str(self.remaining_advance)
