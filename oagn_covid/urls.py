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
    path('master-data/users/', include('users.urls.user_urls')),

    # auth views urls
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # adress,company
    path('master-data/country/', include('master_data.urls.country')),
    path('master-data/province/', include('master_data.urls.province')),
    path('master-data/district/', include('master_data.urls.district')),
    path('master-data/locallevel/', include('master_data.urls.locallevel')),
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
    path('riskAllowance_forms/', include('forms.urls.riskAllowance_forms_urls')),
    # for allowence and OfficeBearer
    path('office_bearer/', include('master_data.urls.officebearer')),
    path('source_budget/', include('master_data.urls.source_budget')),
    path('allowance_type/', include('master_data.urls.allowance_type')),
    path('expense_header/', include('master_data.urls.expense_header')),
    path('cov_hos_managament/', include('master_data.urls.covid_hospital_management_desc')),
    path('committee/', include('master_data.urls.committee')),
    path('relief_type/', include('master_data.urls.relief_type')),
    path('action_plan/', include('master_data.urls.action_plan')),

    path('forms/', include('forms.urls.forms_urls')),

    path('users/', include('users.urls.user_urls')),

    path('', DashboardView.as_view(), name='index'),

]
