from django.urls import path

from master_data.views.employer_type_view import EmployerTypeCreateView, EmployerTypeListView, EmployerTypeListView,\
    EmployerTypeUpdateView, EmployerTypeDeleteView

app_name = 'md-employer_type'

urlpatterns = [
    path('', EmployerTypeListView.as_view(), name='list'),
    path('create/', EmployerTypeCreateView.as_view(), name='create'),
    path('<int:pk>/update/', EmployerTypeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', EmployerTypeDeleteView.as_view(), name='delete'),
]
