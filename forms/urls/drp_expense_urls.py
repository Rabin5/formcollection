from django.urls import path

from forms.views.drp_expense_views import DPRExpenseCreateView, DPRExpenseUpdateView

app_name = 'drp_expense-forms'
urlpatterns = [
    path('create/',
         DPRExpenseCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         DPRExpenseUpdateView.as_view(), name='update'),
]
