from django.urls import path

from master_data.views.contractor_view import ContractorCreateView, ContractorListView,\
    ContractorUpdateView, ContractorDeleteView

app_name = 'md-contractor'

urlpatterns = [
    path('', ContractorListView.as_view(), name='list'),
    path('create/', ContractorCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ContractorUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ContractorDeleteView.as_view(), name='delete'),
]
