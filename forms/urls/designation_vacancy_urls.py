from django.urls import path

from forms.views.designation_vacancy_views import DesignationVacancyCreateView, DesignationVacancyUpdateView

app_name = 'designation_vacancy-forms'
urlpatterns = [
    path('create/',
         DesignationVacancyCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         DesignationVacancyUpdateView.as_view(), name='update'),
]
