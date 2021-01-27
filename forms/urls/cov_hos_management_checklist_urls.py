from django.urls import path

from forms.views.cov_hos_management_checklist_views import CovidHospitalManagementChecklistCreateView, CovidHospitalManagementChecklistUpdateView

app_name = 'covHosManagement-forms'
urlpatterns = [
    path('create',
         CovidHospitalManagementChecklistCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         CovidHospitalManagementChecklistUpdateView.as_view(), name='update'),
]
