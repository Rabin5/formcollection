from django.urls import path

from master_data.views.construction_company_view import ConstructionCompanyCreateView, ConstructionCompanyListView,\
    ConstructionCompanyUpdateView, ConstructionCompanyDeleteView

app_name = 'md-construction'

urlpatterns = [
    path('', ConstructionCompanyListView.as_view(), name='list'),
    path('create/', ConstructionCompanyCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ConstructionCompanyUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ConstructionCompanyDeleteView.as_view(), name='delete'),
]
