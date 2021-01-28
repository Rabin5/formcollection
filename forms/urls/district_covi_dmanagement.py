from django.urls import path

from forms.views.district_covid_management import DistrictCovidManagementCreateView, DistrictCovidManagementUpdateView

app_name = 'district_covid_management'
urlpatterns = [
    path('create',
         DistrictCovidManagementCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         DistrictCovidManagementUpdateView.as_view(), name='update'),
]
