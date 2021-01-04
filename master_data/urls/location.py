from django.urls import path

from master_data.views.location_view import LocationListView, LocationCreateView, LocationUpdateView, LocationDeleteView

app_name = 'md-location'

urlpatterns = [
    path('', LocationListView.as_view(), name='list'),
    path('create/', LocationCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         LocationUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', LocationDeleteView.as_view(), name='delete'),
]
