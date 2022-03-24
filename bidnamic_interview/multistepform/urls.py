from django.urls import path

# import views
from . import views

app_name = 'multistepform'

urlpatterns = [
    path('', views.MultiStepFormView.as_view(), {'step': None})
]