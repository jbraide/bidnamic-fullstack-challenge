from django.urls import path

# import views
from . import views

app_name = 'multistepform'

urlpatterns = [
    path('', views.MultiStepFormView.as_view(), {'step': None}, name='none-step'),
    path('step/<int:step>/', views.MultiStepFormView.as_view(), name='step-parameter'),
    path('clear/', views.ClearFormView.as_view(), name='clear-form'),
    path('feedback/<str:heading>/<str:message>/', views.FeedBackView.as_view(), name='feedback'),
]