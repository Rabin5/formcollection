from django.contrib import admin
from collection import models
# Register your models here.

admin.site.register([
    models.CovHosFormCollection,
    models.ProvinceFormCollection,
    models.InternalAffairFormCollection,
    models.ChiefMinisterOfficeFormCollection,
    models.LocalLevelFormCollection
])
