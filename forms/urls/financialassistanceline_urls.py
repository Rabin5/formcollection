from django.urls import path
from forms.views.financialassistanceline_view import FinancialAssistanceCreateView, FinancialAssistanceUpdateView
app_name = 'finalcial_assistence_create'
urlpatterns = [
    path('create/',
         FinancialAssistanceCreateView.as_view(), name='create'),
    path('<int:pk>/update/',
         FinancialAssistanceUpdateView.as_view(), name='update'),
]
