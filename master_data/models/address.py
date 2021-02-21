from django.db import models
from datetime import datetime


class Country(models.Model):
    name = models.CharField(max_length=300,verbose_name='देश')

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=300,verbose_name='प्रदेश',unique=True)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('id', )


class District(models.Model):
    name = models.CharField(max_length=300,verbose_name='जिल्ला',unique=True)
    province = models.ForeignKey(
        Province, related_name='province_to_district', on_delete=models.CASCADE, null=True, blank=True,verbose_name='प्रदेश')

    def __str__(self):
        return self.name


class LocalLevel(models.Model):
    name = models.CharField(max_length=300,verbose_name='स्थानीय स्तर')
    district = models.ForeignKey(
        District, related_name='local_to_district', on_delete=models.CASCADE, null=True, blank=True,verbose_name='जिल्ला')

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True)
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, null=True, blank=True,verbose_name='प्रदेश')
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, null=True, blank=True)
    local_level = models.ForeignKey(
        LocalLevel, on_delete=models.CASCADE, null=True, blank=True)
    ward = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s %s %s %s" % (self.country, self.province, self.district, self.local_level)
    
    class Meta:
        abstract = True
