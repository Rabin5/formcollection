from django.urls import path

from forms.views.recommendtrainingcenter_views import RecommendTrainingCenterCreateView, RecommendTrainingCenterUpdateView

app_name = 'recommend_traning_center'
urlpatterns = [
    path('create', RecommendTrainingCenterCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         RecommendTrainingCenterUpdateView.as_view(), name='update'),
]
