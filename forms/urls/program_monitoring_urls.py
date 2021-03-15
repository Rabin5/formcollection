from django.urls import path
from forms.views.program_monitoring_views import ProgramMonitoringCreateView, ProgramMonitoringUpdateView

app_name = 'program_monitoring'
urlpatterns = [
    path('create',
         ProgramMonitoringCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ProgramMonitoringUpdateView.as_view(), name='update'),
]
