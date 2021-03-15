from django.urls import path

from forms.views.budgetsubapproval_view import BudgetSubmitApprovalCreateView, BudgetSubmitApprovalUpdateView

app_name = 'budget_apprval'
urlpatterns = [
    path('create',
         BudgetSubmitApprovalCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         BudgetSubmitApprovalUpdateView.as_view(), name='update'),
]
