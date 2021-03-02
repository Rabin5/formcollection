from django.urls import path

from forms.views.foreign_trip_views import ForeignTripCreateView, ForeignTripUpdateView

app_name = 'foreign_trip-forms'
urlpatterns = [
    path('create/',
         ForeignTripCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ForeignTripUpdateView.as_view(), name='update'),
]
