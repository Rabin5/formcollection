from django.urls import path
from forms.views.epi_outbreak_workline_views import EpidemicOutbreakWorklineCreateView, EpidemicOutbreakWorklineUpdateView
app_name = 'epidemic_forms'
urlpatterns = [
    path('epidemic-outbreak/workline/create', EpidemicOutbreakWorklineCreateView.as_view(),
         name='epidemic_outbreak_workline-create'),
    path('epidemic-outbreak/workline/<int:pk>/update/',
         EpidemicOutbreakWorklineUpdateView.as_view(), name='epidemic_outbreak_workline-update'),


]
