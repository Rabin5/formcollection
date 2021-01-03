from django.urls import path

from master_data.views.covid_hospital_management_desc import *

app_name = 'md-cov_hos_managament'

urlpatterns = [
    path('', CovidHospitalManagementChecklistDescriptionListView.as_view(), name='list'),
    path('create/', CovidHospitalManagementChecklistDescriptionCreateView.as_view(), name='create'),
    path('<int:pk>/update', CovidHospitalManagementChecklistDescriptionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', CovidHospitalManagementChecklistDescriptionDeleteView.as_view(), name='delete'),

]
