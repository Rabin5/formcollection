from collection.views.internal_affairs_form_collection_views import (
    InternalAffairFormCollectionCreateView,
    InternalAffairFormCollectionDeleteView,
    InternalAffairFormCollectionListView,
    InternalAffairFormCollectionReviewView,
    InternalAffairFormCollectionUpdateView, 
    internal_affair_submit_form)
from django.urls import path

app_name = 'internal_affairs_forms'
urlpatterns = [
    path('create', InternalAffairFormCollectionCreateView.as_view(), name='create'),
    path('<int:pk>/update', InternalAffairFormCollectionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', InternalAffairFormCollectionDeleteView.as_view(), name='delete'),
    path('list', InternalAffairFormCollectionListView.as_view(), name='list'),
    path('<int:pk>/review', InternalAffairFormCollectionReviewView.as_view(), name='review'),
    path('<int:form_pk>/submit', internal_affair_submit_form, name='submit_form'),
]
