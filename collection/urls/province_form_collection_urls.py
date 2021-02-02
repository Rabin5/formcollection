from collection.views.province_form_collection_views import (
    ProvinceFormCollectionCreateView, ProvinceFormCollectionDeleteView,
    ProvinceFormCollectionListView, ProvinceFormCollectionReviewView,
    ProvinceFormCollectionUpdateView, province_submit_form)
from django.urls import path


app_name = 'province_forms'
urlpatterns = [
    path('create', ProvinceFormCollectionCreateView.as_view(), name='create'),
    path('<int:pk>/update', ProvinceFormCollectionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ProvinceFormCollectionDeleteView.as_view(), name='delete'),
    path('list', ProvinceFormCollectionListView.as_view(), name='list'),
    path('<int:pk>/review', ProvinceFormCollectionReviewView.as_view(), name='review'),
    path('<int:form_pk>/submit', province_submit_form, name='submit_form'),
]
