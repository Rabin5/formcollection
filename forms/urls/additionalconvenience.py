from django.urls import path
from forms.views.additionalconvenience import AdditionalConvenienceCreateView, AdditionalConvenienceUpdateView
app_name = 'asdditional_conven'
urlpatterns = [
    path('create/', AdditionalConvenienceCreateView.as_view(),
         name='create'),
    path('<int:pk>/update/',
         AdditionalConvenienceUpdateView.as_view(), name='update'),


]
