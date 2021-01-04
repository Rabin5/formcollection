from django.urls import path

from master_data.views.committee import *

app_name = 'md-committee'

urlpatterns = [
    path('', CommitteeListView.as_view(), name='list'),
    path('create/', CommitteeCreateView.as_view(), name='create'),
    path('<int:pk>/update', CommitteeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', CommitteeDeleteView.as_view(), name='delete'),

]
