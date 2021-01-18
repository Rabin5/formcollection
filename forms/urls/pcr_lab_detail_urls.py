from django.urls import path

from forms.views.pcr_lab_detail_views import PcrLaboratoryDetailCreateView, PcrLaboratoryDetailUpdateView, get_lab_val

app_name = 'pcrlab-forms'
urlpatterns = [
     path('create',
         PcrLaboratoryDetailCreateView.as_view(), name='create'),
     path('<int:pk>/update',
         PcrLaboratoryDetailUpdateView.as_view(), name='update'),
     path('get_lab_data', get_lab_val, name='get_lab_data')
]
