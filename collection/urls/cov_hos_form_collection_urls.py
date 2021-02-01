from django.urls import path

from collection.views.cov_hos_form_collection_views import CovHosFormCollectionCreateView, CovHosFormCollectionListView, \
    CovHosFormCollectionDeleteView, CovHosFormCollectionUpdateView, FormCollectionReview, submit_form

app_name = 'cov_hos_forms'
urlpatterns = [
    path('create', CovHosFormCollectionCreateView.as_view(), name='create'),
    path('<int:pk>/update', CovHosFormCollectionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', CovHosFormCollectionDeleteView.as_view(), name='delete'),
    path('list', CovHosFormCollectionListView.as_view(), name='list'),
    path('<int:pk>/review', FormCollectionReview.as_view(), name='review'),
    path('<int:form_pk>/submit', submit_form, name='submit_form'),
]
