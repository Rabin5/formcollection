from django.urls import path

from master_data.views.isolation_view import IsolationCenterListView, IsolationCenterCreateView, IsolationCenterUpdateView, IsolationCenterDeleteView

app_name = 'md-isolation'

urlpatterns = [
    path('', IsolationCenterListView.as_view(), name='list'),
    path('create/', IsolationCenterCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         IsolationCenterUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', IsolationCenterDeleteView.as_view(), name='delete'),
]
