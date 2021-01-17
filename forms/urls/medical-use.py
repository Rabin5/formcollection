from django.urls import path

from forms.views.medical_use import MedicalUseCreateView, MedicalUseUpdateView

app_name = 'medical_use'
urlpatterns = [
    path('create/',
         MedicalUseCreateView.as_view(), name='medical_use-create'),
    path('<int:pk>/update',
         MedicalUseUpdateView.as_view(), name='medical_use-update'),
]
