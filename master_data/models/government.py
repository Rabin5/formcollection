from django.db import models
from .hospital import CovidHospital


class GovernmentBodyType(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='वर्णन')
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class GovernmentBody(models.Model):
    # TODO: Address Inheritance
    ordering = ['start_date']
    created = models.DateTimeField(auto_now_add=True)
    # date_end = models.DateTimeField(null=False, auto_now=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='नाम')
    type = models.ForeignKey(
        GovernmentBodyType, on_delete=models.CASCADE, verbose_name='वर्णन', blank=False)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True)
    covid_hospital = models.ForeignKey(
        CovidHospital, on_delete=models.CASCADE, blank=False, verbose_name="अस्पताल")

    def __str__(self) -> str:
        return self.name

class OfficeBearer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class SourceBudget(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

class ExpenseHeader(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

class  Manpower(models.Model):
    pass

class AllowanceType(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class CovidHospitalManagementChecklistDescription(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


class Committee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class ReliefType(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class ActionPlanActivity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
