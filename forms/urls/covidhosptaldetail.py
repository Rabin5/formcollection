from django.urls import path

from forms.views.covidhospitaldetail import CovidHospitalDetailCreateView, CovidHospitalDetailUpdateView

app_name = 'covid_hos_detail'
urlpatterns = [
    path('create',
         CovidHospitalDetailCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         CovidHospitalDetailUpdateView.as_view(), name='update'),
]
