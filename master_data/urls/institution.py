from django.urls import path

from master_data.views.institution import InstitutionListView, InstitutionCreateView, InstitutionUpdateView, InstitutionDeleteView

app_name = 'md-institution'

urlpatterns = [
    path('', InstitutionListView.as_view(), name='list'),
    path('create/', InstitutionCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         InstitutionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete',
         InstitutionDeleteView.as_view(), name='delete'),

]
