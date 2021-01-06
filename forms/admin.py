from django.contrib import admin


from forms import models

admin.site.register([
    models.MedicalExpense,
    models.MedicalExpenseLine,
    models.FormCollection,
    models.RiskAllowance,
    models.RiskAllowanceLine
])
