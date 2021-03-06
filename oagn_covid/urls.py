"""oagn_covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from master_data.models import contractor, convenience_type, designation
from django.contrib import admin
from django.contrib.auth import views as auth_views
from reports.views.dashboard_view import DashboardView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master-data/fiscal-year/', include('master_data.urls.fiscal_year')),
    path('master-data/product/', include('master_data.urls.product')),
    path('master-data/hospital/', include('master_data.urls.hospital')),
    path('master-data/government/', include('master_data.urls.government')),

    # auth views urls
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # adress,company
    path('master-data/address/country/', include('master_data.urls.country')),
    path('master-data/address/province/', include('master_data.urls.province')),
    path('master-data/address/district/', include('master_data.urls.district')),
    path('master-data/address/locallevel/', include('master_data.urls.locallevel')),
    path('master-data/address/', include('master_data.urls.address')),

    path('master-data/companies/', include('master_data.urls.company')),
    # path('master-data/covidhospital/',
    #      include('master_data.urls.covidhospital')),
    path('master-data/location/', include('master_data.urls.location')),
    path('master-data/quanrantinecenter/',
         include('master_data.urls.quarantinecenter')),
    path('master-data/isolationcenter/',
         include('master_data.urls.isolationcenter')),
    path('master-data/importer/', include('master_data.urls.importer')),

    path('master-data/institution/', include('master_data.urls.institution')),
    path('master-data/laboratory/', include('master_data.urls.laboratory')),
    # for allowence and OfficeBearer
    path('master-data/government/office_bearer/',
         include('master_data.urls.officebearer')),
    path('master-data/government/source_budget/',
         include('master_data.urls.source_budget')),
    path('master-data/government/allowance_type/',
         include('master_data.urls.allowance_type')),
    path('master-data/government/expense_header/',
         include('master_data.urls.expense_header')),
    path('master-data/government/cov_hos_managament/',
         include('master_data.urls.covid_hospital_management_desc')),
    path('master-data/government/committee/',
         include('master_data.urls.committee')),
    path('master-data/government/relief_type/',
         include('master_data.urls.relief_type')),
    path('master-data/government/action_plan/',
         include('master_data.urls.action_plan')),
    path('master-data/government/construction_company/',
         include('master_data.urls.construction_company')),
    path('master-data/government/consultant/',
         include('master_data.urls.consultant')),
    path('master-data/government/sub_header/',
         include('master_data.urls.sub_header')),
    path('master-data/government/work_nature/',
         include('master_data.urls.work_nature')),
    path('master-data/government/complaint_type/',
         include('master_data.urls.complaint_type')),
    path('master-data/government/peski_bibaran/',
         include('master_data.urls.peski_bibaran')),
    path('master-data/government/grant_type/',
         include('master_data.urls.grant_type')),
    path('master-data/government/vehicle/',
         include('master_data.urls.vehicle')),
    path('master-data/government/designation/',
         include('master_data.urls.designation')),
    path('master-data/government/project_type/',
         include('master_data.urls.project_type')),
    path('master-data/government/contractor/',
         include('master_data.urls.contractor')),
    path('master-data/government/school/', include('master_data.urls.school')),
    path('master-data/government/convenience_type/',
         include('master_data.urls.convenience_type')),

    path('master-data/government/man_power/',
         include('master_data.urls.man_power')),

    # Forms

    # Covid Hospital
    path('cov-hos/forms/', include('collection.urls.cov_hos_form_collection_urls')),
    path('forms/medical-expense/', include('forms.urls.medical_expense')),
    path('forms/risk-allowance/', include('forms.urls.riskAllowance_forms_urls')),
    path('forms/medical-product-desc/',
         include('forms.urls.med_purchase_desc_urls')),
    path('forms/pcr-lab-detail/', include('forms.urls.pcr_lab_detail_urls')),
    path('forms/pcr-kit-usage/', include('forms.urls.pcr_kit_usage_urls')),
    path('forms/cov-hos-equip/', include('forms.urls.cov_hos_equip_urls')),
    path('forms/fund-receipt-expense/',
         include('forms.urls.fund_receipt_expense')),
    path('forms/medicalreceipt/', include('forms.urls.medicalreceipt_forms_urls')),
    path('forms/medicaluse/', include('forms.urls.medical-use')),
    path('forms/pcr_test/', include('forms.urls.pcr_test')),
    path('forms/rdt_test/', include('forms.urls.rdt_test')),
    path('forms/covid_hos_mainpwer/', include('forms.urls.covid_hos_mainpower')),
    path('forms/covid_hos_detail/', include('forms.urls.covidhosptaldetail')),
    path('forms/iso_mgt_destail/', include('forms.urls.isolationmanagementdetail')),
    path('forms/iso_cons_expenditure/',
         include('forms.urls.isolationconexpenditure')),
    path('forms/quarantine-management-detail/',
         include('forms.urls.quarantine_manage_urls')),
    path('forms/quarantine-construction-expenditure/',
         include('forms.urls.quarantine_contruct_urls')),
    path('forms/cov-hos-management/',
         include('forms.urls.cov_hos_management_checklist_urls')),

    # Province
    path('province/forms/', include('collection.urls.province_form_collection_urls')),
    path('forms/epidemic-outbreak/',
         include('forms.urls.epidemic_outbreak_preparatory_workline')),
    path('forms/district_covid_management/',
         include('forms.urls.district_covi_dmanagement')),
    path('forms/fund-operation/', include('forms.urls.fund_operation_urls')),

    # Internal Affairs
    path('internal-affairs/forms/',
         include('collection.urls.internal_affairs_form_collection_urls')),
    path('forms/action_plan', include('forms.urls.action_plan_implementation_urls')),

    # Chief minister
    path('chief-minister-office/forms/',
         include('collection.urls.chief_minister_form_collection_urls')),
    path('forms/province-institution-management/',
         include('forms.urls.province_institution_management_urls')),

    # Local level
    path('local-level/forms/',
         include('collection.urls.local_level_form_collection_urls')),
    path('forms/ward-relief/', include('forms.urls.ward_relief_urls')),
    path('forms/received-relief/', include('forms.urls.received_relief_urls')),
    path('forms/relief-distribution/',
         include('forms.urls.relief_distribution_urls')),
    path('forms/case_invs_tracing_opt/',
         include('forms.urls.case_invs_tracing_opt')),
     path('forms/case-investigation-tracing/',
         include('forms.urls.case_investigation_tracing_urls')),
    path('forms/relief_procure_dis/',
         include('forms.urls.relief_procure_dis')),
    path('forms/relief_procurement_detail/',
         include('forms.urls.reliefprocurementdetail')),

    # collection six
    path('collection_six/forms/', include('collection.urls.collection_six')),
    path('forms/procurement-auditor/',
         include('forms.urls.procurement_auditor_urls')),
    path('forms/incomplete-construction-work/',
         include('forms.urls.incomplete_construction_work_urls')),
    path('forms/quarterly-program/',
         include('forms.urls.quarterly_program_urls')),
    path('forms/drp-expense/', include('forms.urls.drp_expense_urls')),
    path('forms/yearly-target/', include('forms.urls.yearly_target_urls')),
    path('forms/service_flow/',
         include('forms.urls.service_flow')),
    path('forms/house_map_construction/',
         include('forms.urls.house_map_construction')),
    path('forms/vechile_puches/', include('forms.urls.vechile_purches')),
    path('forms/additional_convenience/',
         include('forms.urls.additionalconvenience')),
    path('forms/conditionalgrant/',
         include('forms.urls.conditionalgrant')),
    path('forms/revenue-distribution/',
         include('forms.urls.revenue_distribution_urls')),
    path('forms/designation-vacancy/',
         include('forms.urls.designation_vacancy_urls')),
    path('forms/contract-desc/', include('forms.urls.contract_desc_urls')),
    path('forms/recover-amount/', include('forms.urls.recover_amount_urls')),
    path('forms/expense-desc/', include('forms.urls.expense_desc_urls')),
    path('forms/integral-advancement/',
         include('forms.urls.integral_advancement_urls')),
    path('forms/teacherdesgination/',
         include('forms.urls.teacherdesignation')),
    path('forms/judicialcommittee/', include('forms.urls.judicialcommittee')),
    path('forms/consumercommitteecons_desc/',
         include('forms.urls.consumercommitteecons_desc')),
    path('forms/financialstatement/', include('forms.urls.financialstatement')),
    path('forms/budgetsubapproval/', include('forms.urls.budgetsubapproval')),
    path('forms/procedure_guide/', include('forms.urls.procedure_guide_urls')),
    path('forms/expenditure_exceeding_allocation/',
         include('forms.urls.expenditure_exceeding_allocation_urls')),
    path('forms/sectoral_budget/', include('forms.urls.sectoral_budget_urls')),
    path('forms/foreign_trip/', include('forms.urls.foreign_trip_urls')),
    path('forms/expenditure_detail/',
         include('forms.urls.expenditure_detail_urls')),
    path('forms/state/partnership-program/',
         include('forms.urls.state_partnership_program_urls')),
    path('forms/local/partnership-program/',
         include('forms.urls.local_partnership_program_urls')),


     # Collection -7
     path('forms/pm_employment_expense/', include('forms.urls.pm_employment_expense_urls')),
     path('forms/registered_unemployment/',
          include('forms.urls.registered_unemployment_urls')),
     path('forms/employment_assessment/',
          include('forms.urls.employment_assessment_urls')),
     path('forms/notify_employee/', include('forms.urls.notify_employee_urls')),
     path('forms/detail_to_employer/',
         include('forms.urls.detail_to_employer_urls')),
     path('forms/transparency_details/',
         include('forms.urls.transparency_detail_urls')),
     path('forms/admin_operative_expense/',
         include('forms.urls.admin_operative_expense_urls')),
     path('forms/meeting_detail/',
         include('forms.urls.meeting_detail_urls')),
     path('forms/program_monitoring/',
         include('forms.urls.program_monitoring_urls')),
     path('forms/contact_details/',
         include('forms.urls.contact_details_urls')),

    path('users/', include('users.urls.user_urls')),
    path('', DashboardView.as_view(), name='index'),

]
