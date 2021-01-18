from django.urls import path

from master_data.views.quarantine_view import QuanrantineCenterListView, QuanrantineCenterCreateView, QuanrantineCenterUpdateView, QuanrantineCenterDeleteView

app_name = 'md-quarantine'

urlpatterns = [
    path('', QuanrantineCenterListView.as_view(), name='list'),
    path('create/', QuanrantineCenterCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         QuanrantineCenterUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', QuanrantineCenterDeleteView.as_view(), name='delete'),
]
