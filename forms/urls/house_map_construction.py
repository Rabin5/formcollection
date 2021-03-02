from django.urls import path

from forms.views.house_map_construction import HouseMapConstructionCreateView, HouseMapConstructionUpdateView

app_name = 'house_map'
urlpatterns = [
    path('create/', HouseMapConstructionCreateView.as_view(), name='create'),
    path('<int:pk>/update', HouseMapConstructionUpdateView.as_view(), name='update'),
]
