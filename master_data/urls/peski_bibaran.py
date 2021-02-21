from django.urls import path

from master_data.views.peski_bibaran_view import PeskiBibaranCreateView, PeskiBibaranListView,\
    PeskiBibaranUpdateView, PeskiBibaranDeleteView

app_name = 'md-peski_bibaran'

urlpatterns = [
    path('', PeskiBibaranListView.as_view(), name='list'),
    path('create/', PeskiBibaranCreateView.as_view(), name='create'),
    path('<int:pk>/update/', PeskiBibaranUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PeskiBibaranDeleteView.as_view(), name='delete'),
]
