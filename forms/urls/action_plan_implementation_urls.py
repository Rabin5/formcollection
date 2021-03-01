from django.urls import path
from forms.views.action_plan_views import ActionPlanImplementationCreateView, ActionPlanImplementationUpdateView
app_name = 'action_plan_forms'
urlpatterns = [
    path('create/', ActionPlanImplementationCreateView.as_view(),
         name='create'),
    path('<int:pk>/update/',
         ActionPlanImplementationUpdateView.as_view(), name='update'),


]
