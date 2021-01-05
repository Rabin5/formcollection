from django.urls import path

from master_data.views.address_view import AddressListView, AddressCreateView, AddressUpdateView, AddressDeleteView

app_name = 'md-address'

urlpatterns = [
    path('', AddressListView.as_view(), name='list'),
    path('create/', AddressCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         AddressUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', AddressDeleteView.as_view(), name='delete'),
]
