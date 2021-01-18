from django.contrib import admin


from forms import models

admin.site.register([
    models.MedicalExpense,
    models.MedicalExpenseLine,
    models.RiskAllowance,
    models.RiskAllowanceLine,
    models.MedicalPurchaseDescription,
    models.MedicalPurchaseDescriptionLine,
    models.PcrLaboratoryDetail,
    models.PcrLaboratoryDetailLine,
    models.PcrKitUsage,
    models.PcrKitUsageLine,
    models.CovidHospitalEquipment,
    models.CovidHospitalEquipmentLine
])
