from django.urls import path

from forms.views.industry_financial_incentive_view import IndustryFinancialIncentiveCreateView, IndustryFinancialIncentiveUpdateView

app_name = 'industry_financial_incentive'
urlpatterns = [
    path('create/',
         IndustryFinancialIncentiveCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         IndustryFinancialIncentiveUpdateView.as_view(), name='update'),
]
