from django.db import models

from .address import Address


class ConstructionCompany(Address):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='नाम',unique=True)

    def __str__(self) -> str:
        if self.name == None:
            return "ERROR- NAME IS NULL"
        return self.name

