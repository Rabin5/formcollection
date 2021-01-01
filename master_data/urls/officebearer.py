from django.urls import path

from master_data.views.officebearer import *

app_name = 'md-offbearer'

urlpatterns = [
    path('', OfficeBearerListView.as_view(), name='list'),
    path('create/', OfficeBearerCreateView.as_view(), name='create'),
    path('<int:pk>/update', OfficeBearerUpdateView.as_view(), name='update'),

]
