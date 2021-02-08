from collection.views.internal_affairs_form_collection_views import (
    InternalAffairFormCollectionCreateView,
    InternalAffairFormCollectionDeleteView,
    InternalAffairFormCollectionListView,
    InternalAffairFormCollectionReviewView,
    InternalAffairFormCollectionUpdateView, 
    ApproveView,
    internal_affair_submit_form
    )
from django.urls import path

app_name = 'internal_affairs_forms'
urlpatterns = [
    path('create', InternalAffairFormCollectionCreateView.as_view(), name='internal_affairs_create'),
    path('<int:pk>/update', InternalAffairFormCollectionUpdateView.as_view(), name='internal_affairs_update'),
    path('<int:pk>/delete', InternalAffairFormCollectionDeleteView.as_view(), name='internal_affairs_delete'),
    path('list', InternalAffairFormCollectionListView.as_view(), name='internal_affairs_list'),
    path('<int:pk>/review/<str:action>', InternalAffairFormCollectionReviewView.as_view(), name='review'),
    path('<int:form_pk>/submit', internal_affair_submit_form, name='submit_form'),
    path('approve/', ApproveView.as_view(), name='review_approve_list'),
]
