from django.urls import path
from forms.views.admin_operative_expense import AdminOperativeExpenseCreateView, AdminOperativeExpenseUpdateView

app_name = 'admin_operative_expense'
urlpatterns = [
    path('create',
         AdminOperativeExpenseCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         AdminOperativeExpenseUpdateView.as_view(), name='update'),
]
