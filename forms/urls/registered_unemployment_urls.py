from django.urls import path

from forms.views.registered_unemployment_views import RegisteredUnemploymentCreateView, RegisteredUnemploymentUpdateView

app_name = 'registered_unemployment-forms'
urlpatterns = [
    path('create/',
         RegisteredUnemploymentCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         RegisteredUnemploymentUpdateView.as_view(), name='update'),
]
