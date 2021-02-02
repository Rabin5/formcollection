from django.urls import path

from forms.views.case_invs_tracing_opt import CaseInvTacingOptCreateView, CaseInvTacingOptUpdateView

app_name = 'case_inv_tracing_opt'
urlpatterns = [
    path('create',
         CaseInvTacingOptCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         CaseInvTacingOptUpdateView.as_view(), name='update'),
]
