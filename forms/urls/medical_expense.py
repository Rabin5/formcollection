from django.urls import path

from forms.views.medical_expense_views import MedExpCreateView, MedExpUpdateView

app_name = 'med_forms'
urlpatterns = [
    path('create', MedExpCreateView.as_view(), name='create'),
    path('<int:pk>/update', MedExpUpdateView.as_view(), name='update'),
]
