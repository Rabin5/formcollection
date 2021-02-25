from django.urls import path

from forms.views.expenditure_exceeding_allocation_views import ExpenditureExceedingAllocationCreateView, ExpenditureExceedingAllocationUpdateView

app_name = 'expenditure_exceeding_allocation-forms'
urlpatterns = [
    path('create/',
         ExpenditureExceedingAllocationCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ExpenditureExceedingAllocationUpdateView.as_view(), name='update'),
]
