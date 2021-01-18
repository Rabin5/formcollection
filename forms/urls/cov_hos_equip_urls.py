from django.urls import path

from forms.views.cov_hos_equipment_views import CovidHospitalEquipmentCreateView, CovidHospitalEquipmentUpdateView

app_name = 'covHosEquip-forms'
urlpatterns = [
    path('create',
         CovidHospitalEquipmentCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         CovidHospitalEquipmentUpdateView.as_view(), name='update'),
]
