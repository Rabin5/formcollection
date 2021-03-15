from django.urls import path

from forms.views.detail_to_employer_views import DetailToEmployerCreateView, DetailToEmployerUpdateView

app_name = 'detail_to_employer-forms'
urlpatterns = [
    path('create/',
         DetailToEmployerCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         DetailToEmployerUpdateView.as_view(), name='update'),
]
