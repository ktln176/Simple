from django.urls import path

from . import views

urlpatterns = [
    path("demo/<int:req_id>", views.demo, name="demo"),
    path("home/", views.home, name="home"),
    path("bot_list/", views.bot_list, name="bot_list"),
    path("", views.start, name="start"),
    path("update_bot", views.update_bot, name="update_bot"),
    path("del_bot", views.del_bot, name="del_bot"),
    path("add_bot", views.add_bot, name="add_bot"),
    path("connect_redis", views.connect_redis, name="connect_redis")
]
