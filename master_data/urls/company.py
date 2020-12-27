from django.urls import path

from master_data.views.company_view import CompanyCreateView, CompanyListView, CompanyUpdateView

app_name = 'md-company'

urlpatterns = [
    path('', CompanyListView.as_view(), name='list'),
    path('create/', CompanyCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         CompanyUpdateView.as_view(), name='update'),
]
