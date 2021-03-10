from django.contrib import admin
from collection import models
from collection.models.collection_six import CollectionSixFormCollection
# Register your models here.

admin.site.register([
    models.CovHosFormCollection,
    models.ProvinceFormCollection,
    models.InternalAffairFormCollection,
    models.ChiefMinisterOfficeFormCollection,
    models.LocalLevelFormCollection,
    models.CollectionSixFormCollection
])
