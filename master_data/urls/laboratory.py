from django.urls import path

from master_data.views.laboratory_view import LaboratoryListView, LaboratoryCreateView, LaboratoryUpdateView, LaboratoryDeleteView

app_name = 'md-laboratory'

urlpatterns = [
    path('', LaboratoryListView.as_view(), name='list'),
    path('create/', LaboratoryCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         LaboratoryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete',
         LaboratoryDeleteView.as_view(), name='delete'),
]
