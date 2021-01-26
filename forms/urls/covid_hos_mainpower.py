from django.urls import path

from forms.views.covid_hos_mainpower import CovidHospitalMainpowerCreateView, CovidHospitalMainpowerUpdateView

app_name = 'covid_hos_mainpower'
urlpatterns = [
    path('create',
         CovidHospitalMainpowerCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         CovidHospitalMainpowerUpdateView.as_view(), name='update'),
]
