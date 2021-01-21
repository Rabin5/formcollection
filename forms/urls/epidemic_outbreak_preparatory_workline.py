from django.urls import path
from forms.views.epi_outbreak_workline_views import EpidemicOutbreakWorklineCreateView
app_name = 'epidemic_forms'
urlpatterns = [
    path('epidemic-outbreak/workline/create', EpidemicOutbreakWorklineCreateView.as_view(),
         name='epidemic_outbreak_workline-create'),


]
