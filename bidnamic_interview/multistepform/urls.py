from django.urls import path

# import views
from . import views

app_name = 'multistepform'

urlpatterns = [
    path('', views.MultiStepFormView.as_view(), {'step': None}, name='none-step'),
    path('step/<int:step>/', views.MultiStepFormView.as_view(), name='step-parameter')
]