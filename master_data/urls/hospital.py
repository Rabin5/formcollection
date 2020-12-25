from django.urls import path

from master_data.views.hospital import CovidHospitalCreateView, CovidHospitalListView, CovidHospitalUpdateView

app_name = 'md-hos'

urlpatterns = [
    path('', CovidHospitalListView.as_view(), name='list'),
    path('create/', CovidHospitalCreateView.as_view(), name='create'),
    path('<int:pk>/update', CovidHospitalUpdateView.as_view(), name='update'),
]
