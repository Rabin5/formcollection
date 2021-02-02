from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models import GovernmentBody
from master_data.models.government import Committee


class ProvinceInstitutionManagement(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody,
        on_delete=models.PROTECT,
        verbose_name="निकायको नामः ",
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.body.name


class ProvinceInstitutionManagementLine(FormLineBaseModel):
    province_institution_management = models.ForeignKey(
        ProvinceInstitutionManagement,
        on_delete=models.PROTECT,
        verbose_name="संस्थागत व्यवस्था: ",
        related_name="lines",
        null=True,
        blank=False,
    )
    committee = models.ForeignKey(
        Committee,
        on_delete=models.PROTECT,
        verbose_name="समिति: ",
        related_name="lines",
        null=True,
        blank=False,
    )
    major_works = models.TextField(null=True, blank=False)

    def __str__(self):
        return str(self.province_institution_management)