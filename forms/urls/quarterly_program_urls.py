from django.urls import path

from forms.views.quarterly_program_views import QuarterlyProgramCreateView, QuarterlyProgramUpdateView

app_name = 'quarterly_program-forms'
urlpatterns = [
    path('create/',
         QuarterlyProgramCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         QuarterlyProgramUpdateView.as_view(), name='update'),
]
