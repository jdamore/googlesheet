from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oauth2callback', views.oauth2callback, name='oauth2callback'),
]