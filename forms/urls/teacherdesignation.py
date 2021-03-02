
from django.urls import path

from forms.views.teacherdesignation import TeacherDesginationCreateView, TeacherDesginationUpdateView

app_name = 'techer_desg'
urlpatterns = [
    path('create/',
         TeacherDesginationCreateView.as_view(), name='create'),
    path('<int:pk>/update/',
         TeacherDesginationUpdateView.as_view(), name='update'),
]
