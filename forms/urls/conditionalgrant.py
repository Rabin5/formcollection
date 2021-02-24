from django.urls import path
from forms.views.conditionalgrant import ConditionalGrantCreateView, ConditionalGrantUpdateView
app_name = 'cnl_grant'
urlpatterns = [
    path('create/', ConditionalGrantCreateView.as_view(),
         name='create'),
    path('<int:pk>/update/',
         ConditionalGrantUpdateView.as_view(), name='update'),
]
