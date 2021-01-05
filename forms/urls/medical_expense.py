from django.urls import path

from forms.views.medical_expense_views import MedExpCreateView, MedExpUpdateView

app_name = 'med-forms'
urlpatterns = [
    path('create', MedExpCreateView.as_view(), name='med_exp-create'),
    path('<int:pk>/update', MedExpUpdateView.as_view(), name='med_exp-update'),
]
