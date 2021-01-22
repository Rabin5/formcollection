from django.contrib import admin

from master_data import models

admin.site.register(models.FiscalYear)
admin.site.register(models.Product)
admin.site.register(models.UnitOfMeasure)
admin.site.register(models.Hospital)
admin.site.register(models.CovidHospital)
admin.site.register(models.GovernmentBodyType)
admin.site.register(models.GovernmentBody)
admin.site.register(models.OfficeBearer)
admin.site.register(models.AllowanceType)
admin.site.register(models.Laboratory)
admin.site.register(models.Address)
admin.site.register(models.Institution)
admin.site.register(models.IsolationCenter)
admin.site.register(models.ProcurementMethod)
admin.site.register(models.CovidHospitalManagementChecklistDescription)