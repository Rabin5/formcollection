from django.urls import path

from master_data.views.district_view import DistrictListView, DistrictCreateView, DistrictUpdateView

app_name = 'md-district'

urlpatterns = [
    path('', DistrictListView.as_view(), name='list'),
    path('create/', DistrictCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         DistrictUpdateView.as_view(), name='update'),
]
