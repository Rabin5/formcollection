from django.db import models
from datetime import datetime
from .address import Address


class Location(Address):
    name = models.CharField(max_length=300)

    class Meta:
        abstract = True


class QuanrantineCenter(Location):
    pass


class IsolationCenter(Location):
    def __str__(self):
        return self.name


class Company(Address):
    name = models.CharField(max_length=300)
    date_establishment = models.DateField(null=True, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True


class Importer(Company):
    pass


class Laboratory(Company):
    capacity_daily_test = models.IntegerField()


class Institution(Company):
    pass
