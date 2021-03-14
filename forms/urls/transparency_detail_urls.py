from django.urls import path
from forms.views.transparency_detail import TransparencyDetailCreateView, TransparencyDetailUpdateView

app_name = 'transparency_detail'
urlpatterns = [
    path('create',
         TransparencyDetailCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         TransparencyDetailUpdateView.as_view(), name='update'),
]
