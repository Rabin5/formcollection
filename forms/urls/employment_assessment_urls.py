from django.urls import path

from forms.views.employment_assessment_views import EmploymentAssessmentCreateView, EmploymentAssessmentUpdateView

app_name = 'employment_assessment-forms'
urlpatterns = [
    path('create/',
         EmploymentAssessmentCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         EmploymentAssessmentUpdateView.as_view(), name='update'),
]
