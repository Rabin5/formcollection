from django.urls import path

from master_data.views.source_budget import *

app_name = 'md-source_budget'

urlpatterns = [
    path('', SourceBudgetListView.as_view(), name='list'),
    path('create/', SourceBudgetCreateView.as_view(), name='create'),
    path('<int:pk>/update', SourceBudgetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', SourceBudgetDeleteView.as_view(), name='delete'),

]
