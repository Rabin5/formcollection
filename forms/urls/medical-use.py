from django.urls import path

from forms.views.medical_use import MedicalUseCreateView, MedicalUseUpdateView

app_name = 'medical_use-forms'
urlpatterns = [
    path('create/',
         MedicalUseCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         MedicalUseUpdateView.as_view(), name='update'),
]
