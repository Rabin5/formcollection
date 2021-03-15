from django.urls import path
from forms.views.contact_details_views import ContactDetailsCreateView, ContactDetailsUpdateView

app_name = 'contact_details'
urlpatterns = [
    path('create',
         ContactDetailsCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ContactDetailsUpdateView.as_view(), name='update'),
]
