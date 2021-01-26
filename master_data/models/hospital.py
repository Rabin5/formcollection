from django.db import models


class Hospital(models.Model):
    # TODO: Inheritance location
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='नाम')

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class CovidHospital(Hospital):
    # TODO: Address Inheritance
    ordering = ['start_date']
    data_created = models.DateTimeField(auto_now_add=True)
    # date_end = models.DateTimeField(null=False, auto_now=True)
    type = models.CharField(
        max_length=255, verbose_name='वर्णन', blank=False, null=False)
    date_announcement = models.CharField(
        max_length=15, blank=False, null=False, verbose_name='मिति घोषित', default='01/01/2000')

    def __str__(self) -> str:
        return self.name

    def get_children():
        pass
