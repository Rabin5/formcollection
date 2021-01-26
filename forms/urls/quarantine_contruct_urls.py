from django.urls import path

from forms.views.quarantine_construct_expenditure_views import QuarantineConstructionExpenditureCreateView, QuarantineConstructionExpenditureUpdateView

app_name = 'quarantine_construct_forms'
urlpatterns = [
    path('create', QuarantineConstructionExpenditureCreateView.as_view(), name='create'),
    path('<int:pk>/update', QuarantineConstructionExpenditureUpdateView.as_view(), name='update'),
]