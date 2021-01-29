from django.urls import path

from forms.views.pcr_test import PcrTestCreateView, PcrTestUpdateView

app_name = 'pcr_test-forms'
urlpatterns = [
    path('create/',
         PcrTestCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         PcrTestUpdateView.as_view(), name='update'),
]
