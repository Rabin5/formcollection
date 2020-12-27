from django.urls import path

from master_data.views.localLevel_view import LocalLevelListView, LocalLevelCreateView, LocalLevelUpdateView

app_name = 'md-locallevel'

urlpatterns = [
    path('', LocalLevelListView.as_view(), name='list'),
    path('create/', LocalLevelCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         LocalLevelUpdateView.as_view(), name='update'),
]
