from django.urls import path

from master_data.views.importer_view import ImporterListView, ImporterCreateView, ImporterUpdateView, ImporterDeleteView

app_name = 'md-importer'

urlpatterns = [
    path('', ImporterListView.as_view(), name='list'),
    path('create/', ImporterCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ImporterUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ImporterDeleteView.as_view(), name='delete'),
]
