from django.urls import path

from . import views

urlpatterns = [
    path('', views.module_start),
    path('login', views.login),
    path('home', views.home)
]
