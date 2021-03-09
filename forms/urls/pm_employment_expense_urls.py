from django.urls import path

from forms.views.pm_employment_expense_views import PMEmploymentExpenseCreateView, PMEmploymentExpenseUpdateView

app_name = 'pm_employment_expense-forms'
urlpatterns = [
    path('create/',
         PMEmploymentExpenseCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         PMEmploymentExpenseUpdateView.as_view(), name='update'),
]
