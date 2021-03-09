from django.urls import path

from forms.views.notify_employee_views import NotifyEmployeeCreateView, NotifyEmployeeUpdateView

app_name = 'notify_employee-forms'
urlpatterns = [
    path('create/',
         NotifyEmployeeCreateView.as_view(), name='create'),
    path('<int:pk>/update',
         NotifyEmployeeUpdateView.as_view(), name='update'),
]
