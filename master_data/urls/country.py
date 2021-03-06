from django.urls import path

from master_data.views.country_view import CountryListView, CountryCreateView, CountryUpdateView, CountryDeleteView

app_name = 'md-country'

urlpatterns = [
    path('', CountryListView.as_view(), name='list'),
    path('create/', CountryCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         CountryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete',
         CountryDeleteView.as_view(), name='delete'),

]
