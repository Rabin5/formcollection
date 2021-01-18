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
])
