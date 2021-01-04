from django.urls import path

from master_data.views.action_plan import *

app_name = 'md-action_plan'

urlpatterns = [
    path('', ActionPlanActivityListView.as_view(), name='list'),
    path('create/', ActionPlanActivityCreateView.as_view(), name='create'),
    path('<int:pk>/update', ActionPlanActivityUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ActionPlanActivityDeleteView.as_view(), name='delete'),

]
