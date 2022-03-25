from django.urls import path

# import views
from . import views

app_name = 'view-applications'

urlpatterns = [
    path('', views.ViewAllApplications.as_view(), name='all-applications'),
    path('remove-application-record/<int:id>/', views.RemoveApplicationRecord.as_view(), name='remove-application-record'),
]