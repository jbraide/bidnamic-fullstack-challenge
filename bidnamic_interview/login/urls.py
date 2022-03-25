from django.urls import path

# import login view
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.Login.as_view(), name='login')
]