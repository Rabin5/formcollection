from django.db import models
from datetime import datetime


class LocalLevel(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=300)
    local_level = models.ForeignKey(LocalLevel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=300)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True)
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, null=True, blank=True)
    local_level = models.ForeignKey(
        LocalLevel, on_delete=models.CASCADE, null=True, blank=True)
    ward = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s %s %s %s" % (self.country, self.province, self.district, self.local_level)
