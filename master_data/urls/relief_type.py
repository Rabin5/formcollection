from django.urls import path

from master_data.views.relief_type import *

app_name = 'md-relief_type'

urlpatterns = [
    path('', ReliefTypeListView.as_view(), name='list'),
    path('create/', ReliefTypeCreateView.as_view(), name='create'),
    path('<int:pk>/update', ReliefTypeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ReliefTypeDeleteView.as_view(), name='delete'),

]
