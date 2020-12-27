from django.urls import path

from master_data.views.covidhospital_view import CovidhospitalCreateView, CovidhospitalListView, CovidhospitalUpdateView

app_name = 'md-covidhospital'

urlpatterns = [
    path('', CovidhospitalListView.as_view(), name='list'),
    path('create/', CovidhospitalCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         CovidhospitalUpdateView.as_view(), name='update'),
]
