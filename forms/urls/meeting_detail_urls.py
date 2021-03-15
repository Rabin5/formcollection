from django.urls import path
from forms.views.meeting_detail import MeetingDetailCreateView, MeetingDetailUpdateView

app_name = 'meeting_detail'
urlpatterns = [
    path('create',
         MeetingDetailCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         MeetingDetailUpdateView.as_view(), name='update'),
]
