from django.urls import path

from . import views

urlpatterns = [
    path("demo/<int:req_id>", views.demo, name="demo"),
    path("home/", views.home, name="home"),
    path("bot_list/", views.bot_list, name="bot_list"),
    path("", views.start, name="start")
]
