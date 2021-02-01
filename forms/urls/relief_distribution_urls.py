from django.urls import path

from forms.views.relief_distribution_views import ReliefDistributionExpenseCreateView, ReliefDistributionExpenseUpdateView

app_name = 'relief_distribution'
urlpatterns = [
    path('create',
         ReliefDistributionExpenseCreateView.as_view(), name='relief_distribution_create'),
    path('<int:pk>/update',
         ReliefDistributionExpenseUpdateView.as_view(), name='relief_distribution_update'),
]
