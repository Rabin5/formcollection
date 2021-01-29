from django.urls import path

from forms.views.rdt_test import RdtTestCreateView, RdtTestUpdateView

app_name = 'rdt_test-forms'
urlpatterns = [
    path('create/',
         RdtTestCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         RdtTestUpdateView.as_view(), name='update'),
]
