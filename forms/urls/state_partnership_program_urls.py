from django.urls import path

from forms.views.state_partnership_program_views import StatePartnershipProgramtCreateView, StatePartnershipProgramtUpdateView

app_name = 'state_partnership_program-forms'
urlpatterns = [
    path('create/',
         StatePartnershipProgramtCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         StatePartnershipProgramtUpdateView.as_view(), name='update'),
]
