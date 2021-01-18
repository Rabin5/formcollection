from django.urls import path

from forms.views.fund_receipt_expense_views import FundReceiptExpenseCreateView, FundReceiptExpenseUpdateView

app_name = 'fund_receipt_expense'
urlpatterns = [
    path('create', FundReceiptExpenseCreateView.as_view(), name='create'),
    path('<int:pk>/update', FundReceiptExpenseUpdateView.as_view(), name='update'),
]
