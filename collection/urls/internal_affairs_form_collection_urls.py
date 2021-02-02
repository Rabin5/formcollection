from django.urls import path

from collection.views.internal_affairs_form_collection_views import InternalAffairFormCollectionCreateView, InternalAffairFormCollectionListView, \
    InternalAffairFormCollectionDeleteView, InternalAffairFormCollectionUpdateView

app_name = 'internal_affairs_forms'
urlpatterns = [
    path('create', InternalAffairFormCollectionCreateView.as_view(), name='create'),
    path('<int:pk>/update', InternalAffairFormCollectionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', InternalAffairFormCollectionDeleteView.as_view(), name='delete'),
    path('list', InternalAffairFormCollectionListView.as_view(), name='list'),
]
