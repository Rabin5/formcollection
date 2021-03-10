from django.urls import path

from forms.views.judicialcommittee_view import JudicialCommitteeCreateView, JudicialCommitteeUpdateView

app_name = 'judicial-com'
urlpatterns = [
    path('create',
         JudicialCommitteeCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         JudicialCommitteeUpdateView.as_view(), name='update'),
]
