from django.contrib import admin

from master_data import models

admin.site.register(models.FiscalYear)
admin.site.register(models.address.Country)
admin.site.register(models.address.Province)
admin.site.register(models.address.District)
admin.site.register(models.address.LocalLevel)
admin.site.register(models.IsolationCenter)
admin.site.register(models.ProcurementMethod)
admin.site.register(models.UnitOfMeasure)
admin.site.register(models.CovidHospital)
admin.site.register(models.GovernmentBodyType)
admin.site.register(models.GovernmentBody)
admin.site.register(models.OfficeBearer)
admin.site.register(models.AllowanceType)
admin.site.register(models.Laboratory)
admin.site.register(models.ActionPlanActivity)
admin.site.register(models.Manpower)
admin.site.register(models.Institution)
admin.site.register(models.CovidHospitalManagementChecklistDescription)

admin.site.register(models.ExpenseHeader)
admin.site.register(models.Product)
admin.site.register(models.ReliefType)
admin.site.register(models.ComplaintType)
admin.site.register(models.PeskiBibaran)



