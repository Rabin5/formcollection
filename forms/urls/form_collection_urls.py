from django.urls import path

from forms.views.form_collection_views import FormCollectionCreateView, FormCollectionListView, \
    FormCollectionDeleteView, FormCollectionUpdateView, FormCollectionReview, submit_form

app_name = 'forms'
urlpatterns = [
    path('create', FormCollectionCreateView.as_view(), name='create'),
    path('<int:pk>/update', FormCollectionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', FormCollectionDeleteView.as_view(), name='delete'),
    path('<int:pk>/review', FormCollectionReview.as_view(), name='review'),
    path('<int:form_pk>/submit', submit_form, name='submit_form'),
    path('list', FormCollectionListView.as_view(), name='list'),
]
