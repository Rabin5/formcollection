from django.urls import path

from forms.views.procurement_auditor_views import ProcurementAuditorCreateView, ProcurementAuditorUpdateView

app_name = 'procurement_auditor-forms'
urlpatterns = [
    path('create/',
         ProcurementAuditorCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ProcurementAuditorUpdateView.as_view(), name='update'),
]
