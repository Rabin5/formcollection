from django.db import models
from datetime import datetime
from .address import Address


class Location(Address):
    name = models.CharField(max_length=300)


class QuanrantineCenter(Location):
    pass


class IsolationCenter(Location):
    pass


class Company(Address):
    name = models.CharField(max_length=300)
    date_establishment = models.DateField(null=False)

    def __str__(self):
        return self.name


class Importer(Company):
    pass


class Laboratory(Company):
    capacity_daily_test = models.IntegerField()


class Institution(Company):
    pass
