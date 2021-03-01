from django.urls import path

from forms.views.expense_desc_views import ExpenseDescCreateView, ExpenseDescUpdateView

app_name = 'expense_desc-forms'
urlpatterns = [
    path('create/',
         ExpenseDescCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ExpenseDescUpdateView.as_view(), name='update'),
]
