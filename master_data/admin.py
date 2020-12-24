from django.contrib import admin

from master_data import models

admin.site.register(models.FiscalYear)
admin.site.register(models.Product)
admin.site.register(models.UnitOfMeasure)
admin.site.register(models.Hospital)
admin.site.register(models.CovidHospital)
