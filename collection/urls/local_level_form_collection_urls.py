from collection.views.local_level_form_collection_views import (
    LocalLevelFormCollectionCreateView, LocalLevelFormCollectionDeleteView,
    LocalLevelFormCollectionListView, LocalLevelFormCollectionReviewView,
    LocalLevelFormCollectionUpdateView, local_level_submit_form)
from django.urls import path

app_name = 'local_level_forms'
urlpatterns = [
    path('create', LocalLevelFormCollectionCreateView.as_view(), name='create'),
    path('<int:pk>/update', LocalLevelFormCollectionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', LocalLevelFormCollectionDeleteView.as_view(), name='delete'),
    path('list', LocalLevelFormCollectionListView.as_view(), name='list'),
    path('<int:pk>/review', LocalLevelFormCollectionReviewView.as_view(), name='review'),
    path('<int:form_pk>/submit', local_level_submit_form, name='submit_form'),
]
