
from forms.models.local_partnership_program import LocalPartnershipProgramLine

from forms.models.covidhospitaldetail import CovidHospitalDetail

from django.contrib import admin


from forms import models

admin.site.register([
    models.MedicalExpense,
    models.MedicalExpenseLine,
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
    models.CaseInvestigationTracing,
    models.CaseInvestigationTracingLine,
    models.ProvinceInstitutionManagement,
    models.ProvinceInstitutionManagementLine,
    models.QuarantineManagementDetail,
    models.QuarantineManagementDetailLine,
    models.CovidHospitalManagementChecklist,
    models.CovidHospitalManagementChecklistLine,
    models.FundOperation,
    models.FundOperationLine,
    models.WardReliefProcureDistribution,
    models.WardReliefProcureDistributionLine,
    models.ReceivedReliefDetail,
    models.ReceivedReliefDetailLine,
    models.ReliefDistributionExpense,
    models.ReliefDistributionExpenseLine,
    models.ProjectType,
    models.LocalPartnershipProgramLine,
    models.LocalPartnershipProgram,
    models.DesignationVacancy,
    models.DesignationVacancyLine,
    models.ContractDesc,
    models.ContractDescLine,
    models.CovidHospitalDetail,
    models.CovidHospitalDetailLine,
    models.ConditionalGrant,
    models.ConditionalGrantLine,
    models.ServiceFlow,
    models.ServiceFlowLine,
    models.ContactDetails,
    models.ContactDetailsLine
])
