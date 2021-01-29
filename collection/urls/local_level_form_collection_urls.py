from django.urls import path

from collection.views.local_level_form_collection_views import LocalLevelFormCollectionCreateView, LocalLevelFormCollectionListView, \
    LocalLevelFormCollectionDeleteView, LocalLevelFormCollectionUpdateView

app_name = 'local_level_forms'
urlpatterns = [
    path('create', LocalLevelFormCollectionCreateView.as_view(), name='create'),
    path('<int:pk>/update', LocalLevelFormCollectionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', LocalLevelFormCollectionDeleteView.as_view(), name='delete'),
    path('list', LocalLevelFormCollectionListView.as_view(), name='list'),
]
