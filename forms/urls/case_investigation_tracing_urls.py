from django.urls import path
from forms.views.case_investigation_views import CaseInvestigationTracingCreateView, CaseInvestigationTracingUpdateView
app_name = 'case_investigation_forms'
urlpatterns = [
    path('create/', CaseInvestigationTracingCreateView.as_view(),
         name='conditional-grant-create'),
    path('<int:pk>/update/',
         CaseInvestigationTracingUpdateView.as_view(), name='conditional-grant-update'),
]
