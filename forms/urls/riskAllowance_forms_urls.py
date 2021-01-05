from django.urls import path

from forms.views.risk_allowance_views import RiskAllowanceCreateView, RiskAllowanceUpdateView

app_name = 'risk-forms'
urlpatterns = [
    path('create',
         RiskAllowanceCreateView.as_view(), name='risk_allowance-create'),
    path('<int:pk>/update',
         RiskAllowanceUpdateView.as_view(), name='risk_allowance-update'),
]
