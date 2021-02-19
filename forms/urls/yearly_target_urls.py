from django.urls import path

from forms.views.yearly_target_views import YearlyTargetCreateView, YearlyTargetUpdateView

app_name = 'yearly_target-forms'
urlpatterns = [
    path('create/',
         YearlyTargetCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         YearlyTargetUpdateView.as_view(), name='update'),
]
