from django.urls import path

from master_data.views.hospital import CovidHospitalCreateView, CovidHospitalListView, CovidHospitalUpdateView, \
        HospitalCreateView, HospitalListView, HospitalUpdateView, CovidHospitalDeleteView, HospitalDeleteView

app_name = 'md-hos'

urlpatterns = [
    # path('', HospitalListView.as_view(), name='list'),
    # path('create/', HospitalCreateView.as_view(), name='create'),
    # path('<int:pk>/update', HospitalUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete', HospitalDeleteView.as_view(), name='delete'),
    path('cov/', CovidHospitalListView.as_view(), name='cov_list'),
    path('cov/create/', CovidHospitalCreateView.as_view(), name='cov_create'),
    path('cov/<int:pk>/update', CovidHospitalUpdateView.as_view(), name='cov_update'),
    path('cov/<int:pk>/delete', CovidHospitalDeleteView.as_view(), name='cov_delete'),
]
