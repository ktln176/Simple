from django.http import HttpResponse
from django.shortcuts import render
from django_redis import get_redis_connection

from .models import Botlist


# Create your views here.

def demo(request, req_id: str):
    return HttpResponse('Demo' + str(req_id))


def home(request):
    return HttpResponse('Home')


def start(request):
    return HttpResponse('Start')


def bot_list(request):
    select_bot_list = Botlist.objects.all()
    print(select_bot_list)
    return render(request, 'bot_list.html')


def add_bot(request):
    """添加机器人"""
    add_list = [
        Botlist(name="添加机器人1", status=0, task_name='')
    ]
    Botlist.objects.bulk_create(add_list)
    return render(request, 'add_bot.html')


def update_bot(request):
    """修改机器人"""
    target_bot = Botlist.objects.get(name='添加机器人1')
    target_bot.task_name = '添加任务1'
    target_bot.save()
    return render(request, 'update_bot.html')


def del_bot(request):
    """修改机器人"""
    target_bot = Botlist.objects.get(name='添加机器人1')
    target_bot.delete()
    return render(request, 'del_bot.html')


def connect_redis(request):
    conn = get_redis_connection('default')
    a = conn.get('name')
    print(a)
    return render(request, 'redis.html')
