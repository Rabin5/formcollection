from django.urls import path

from master_data.views.expense_header import *

app_name = 'md-expense_header'

urlpatterns = [
    path('', ExpenseHeaderListView.as_view(), name='list'),
    path('create/', ExpenseHeaderCreateView.as_view(), name='create'),
    path('<int:pk>/update', ExpenseHeaderUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ExpenseHeaderDeleteView.as_view(), name='delete'),

]
