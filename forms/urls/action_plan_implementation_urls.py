from django.urls import path
from forms.views.action_plan_views import ActionPlanImplementationCreateView,ActionPlanImplementationUpdateView
app_name = 'action_plan_forms'
urlpatterns = [
    path('action-plan/implementation/create/', ActionPlanImplementationCreateView.as_view(),
         name='action_plan_implementation-create'),
    path('action-plan/implementation/<int:pk>/update/',
         ActionPlanImplementationUpdateView.as_view(), name='action_plan_implementation-update'),


]
