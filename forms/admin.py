from django.contrib import admin


from forms import models

admin.site.register([
    models.MedicalExpense,
    models.MedicalExpenseLine,
    models.FormCollection,
    models.RiskAllowance,
    models.RiskAllowanceLine,
    models.MedicalReceipt,
    models.MedicalReceiptLine,
    models.MedicalUse,
    models.MedicalUseLine,
    models.PcrTestComplianceDetail,
    models.PcrTestComplianceDetailLine,
    models.RdtTestDetail,
    models.RdtTestDetailLine,
    models.MedicalPurchaseDescription,
    models.MedicalPurchaseDescriptionLine,
    models.PcrLaboratoryDetail,
    models.PcrLaboratoryDetailLine,
    models.PcrKitUsage,
    models.PcrKitUsageLine,
    models.CovidHospitalEquipment,
    models.CovidHospitalEquipmentLine,
    models.FundReceiptExpense,
    models.FundReceiptExpenseLine,
    models.EpidemicOutbreakPreparatoryWork,
    models.EpidemicOutbreakPreparatoryWorkLine,
    models.ActionPlanImplementation,
    models.ActionPlanImplementationLine,
])
