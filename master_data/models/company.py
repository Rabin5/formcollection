from django.db import models
from datetime import datetime
from .address import Address


class Location(Address):
    name = models.CharField(max_length=300, verbose_name='नाम')

    class Meta:
        abstract = True
    
    def __str__(self):
        if self.local_level and self.district:
            return f"{self.name}, {self.local_level.name}, {self.district.name}"
        else:
            return self.name


class QuanrantineCenter(Location):
    pass


class IsolationCenter(Location):
    pass


class Company(Address):
    name = models.CharField(max_length=300, verbose_name='नाम')
    date_establishment = models.DateField(
        null=True, blank=False, verbose_name='स्थापना मिति'
    )

    def __init__(self, *args, **kwargs) -> None:
        super(Company, self).__init__(*args, **kwargs)

    def __str__(self):
        if self.local_level and self.district:
            return f"{self.name}, {self.local_level.name}, {self.district.name}"
        else:
            return self.name
    
    class Meta:
        abstract = True


class Importer(Company):
    pass


class Laboratory(Company):
    capacity_daily_test = models.IntegerField(default=0, verbose_name='दैनिक परीक्षण क्षमता')


class Institution(Company):
    pass
