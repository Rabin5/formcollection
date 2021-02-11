from django.urls import path

from master_data.views.consultant_view import ConsultantCreateView, ConsultantListView,\
    ConsultantUpdateView, ConsultantDeleteView

app_name = 'md-consultant'

urlpatterns = [
    path('', ConsultantListView.as_view(), name='list'),
    path('create/', ConsultantCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ConsultantUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ConsultantDeleteView.as_view(), name='delete'),
]
