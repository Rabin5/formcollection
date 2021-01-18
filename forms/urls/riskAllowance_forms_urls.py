from django.urls import path

from forms.views.risk_allowance_views import RiskAllowanceCreateView, RiskAllowanceUpdateView

app_name = 'risk_forms'
urlpatterns = [
    path('create',
         RiskAllowanceCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         RiskAllowanceUpdateView.as_view(), name='update'),
]
