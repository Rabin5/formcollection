from django.urls import path
from master_data.views.man_power import ManpowerListView, ManpowerCreateView, ManpowerUpdateView, ManpowerDeleteView
app_name = 'md-manpower'
urlpatterns = [
    path('', ManpowerListView.as_view(), name='list'),
    path('create/', ManpowerCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ManpowerUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ManpowerDeleteView.as_view(), name='delete'),
]
