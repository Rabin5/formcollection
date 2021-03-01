from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models.designation import Designation


class DesignationVacancy(FormBaseModel):
    pass


class DesignationVacancyLine(FormLineBaseModel):
    designation=models.ForeignKey(Designation,on_delete=models.CASCADE,related_name='designation_vacancy_lines',verbose_name='स्वीकृत पद')
    total = models.PositiveIntegerField(verbose_name='जम्मा पदपूर्ति')
    num_internal = models.PositiveIntegerField(verbose_name='आन्तरिक पदपूर्ति')
    num_union = models.PositiveIntegerField(verbose_name='संख्या')
    num_filled = models.PositiveIntegerField(verbose_name='साबिक स्थानीय निकायमा कार्यरत')
    remaining_vacancy = models.PositiveIntegerField(verbose_name='रिक्त पद')
    num_former_body = models.PositiveIntegerField(verbose_name='संघबाट समायोजन भई आएका')
    remarks = models.CharField(max_length=300,blank=True, null=True, verbose_name='कैफियत')
    designation_vacancy = models.ForeignKey(
        DesignationVacancy, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
