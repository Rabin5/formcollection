from django.urls import path

from forms.views.local_partnership_program_views import LocalPartnershipProgramtCreateView, LocalPartnershipProgramtUpdateView

app_name = 'local_partnership_program-forms'
urlpatterns = [
    path('create/',
         LocalPartnershipProgramtCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         LocalPartnershipProgramtUpdateView.as_view(), name='update'),
]
