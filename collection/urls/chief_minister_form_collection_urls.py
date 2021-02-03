from collection.views.chief_minister_form_collection_views import (
    ChiefMinisterOfficeFormCollectionCreateView,
    ChiefMinisterOfficeFormCollectionDeleteView,
    ChiefMinisterOfficeFormCollectionListView,
    ChiefMinisterOfficeFormCollectionReviewView,
    ChiefMinisterOfficeFormCollectionUpdateView, 
    chief_minister_submit_form)
from django.urls import path

app_name = 'chief_minister_forms'
urlpatterns = [
    path('create', ChiefMinisterOfficeFormCollectionCreateView.as_view(), name='create'),
    path('<int:pk>/update', ChiefMinisterOfficeFormCollectionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ChiefMinisterOfficeFormCollectionDeleteView.as_view(), name='delete'),
    path('list', ChiefMinisterOfficeFormCollectionListView.as_view(), name='list'),
    path('<int:pk>/review', ChiefMinisterOfficeFormCollectionReviewView.as_view(), name='review'),
    path('<int:form_pk>/submit', chief_minister_submit_form, name='submit_form'),
]
