from django.urls import path

from forms.views.consumercommitteecons_desc_view import ConsumercomConsDespCreateView, ConsumercomConsDespUpdateView

app_name = 'consumer-com-des'
urlpatterns = [
    path('create',
         ConsumercomConsDespCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         ConsumercomConsDespUpdateView.as_view(), name='update'),
]
