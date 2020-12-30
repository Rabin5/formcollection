from django.urls import path

from forms.views.risk_allowance_views import RiskAllowanceCreateView, RiskAllowanceUpdateView

app_name = 'forms'
urlpatterns = [
    path('risk-allowance/create',
         RiskAllowanceCreateView.as_view(), name='risk_allowance-create'),
    path('risk-allowance/<int:pk>/update',
         RiskAllowanceUpdateView.as_view(), name='risk_allowance-update'),
]
