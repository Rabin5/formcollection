from django.urls import path

from master_data.views.vehicle_view import VehicleCreateView, VehicleListView,\
    VehicleUpdateView, VehicleDeleteView

app_name = 'md-vehicle'

urlpatterns = [
    path('', VehicleListView.as_view(), name='list'),
    path('create/', VehicleCreateView.as_view(), name='create'),
    path('<int:pk>/update/', VehicleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', VehicleDeleteView.as_view(), name='delete'),
]
