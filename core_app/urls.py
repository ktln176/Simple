from django.urls import path

from . import views

urlpatterns = [
    path('', views.core_start),
    path('home', views.home)
]
