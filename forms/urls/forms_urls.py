from django.urls import path

from forms.views.medical_expense_views import MedExpCreateView, MedExpUpdateView

app_name = 'forms'
urlpatterns = [
    path('medical-expense/create', MedExpCreateView.as_view(), name='med_exp-create'),
    path('medical-expense/<int:pk>/update', MedExpUpdateView.as_view(), name='med_exp-update'),
]
