from django.urls import path

from forms.views.form_collection_views import FormCollectionCreateView

app_name = 'forms'
urlpatterns = [
    path('create', FormCollectionCreateView.as_view(), name='create'),
]
