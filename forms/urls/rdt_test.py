from django.urls import path

from forms.views.rdt_test import RdtTestCreateView, RdtTestUpdateView

app_name = 'rdt_test'
urlpatterns = [
    path('create/',
         RdtTestCreateView.as_view(), name='rdt_test-create'),
    path('<int:pk>/update',
         RdtTestUpdateView.as_view(), name='rdt_test-update'),
]
