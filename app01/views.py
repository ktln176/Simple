from django.http import HttpResponse
from django.shortcuts import render
from .models import App01Botlist


# Create your views here.

def demo(request, req_id: str):
    return HttpResponse('Demo' + str(req_id))


def home(request):
    return HttpResponse('Home')


def start(request):
    return HttpResponse('Start')


def bot_list(request):
    select_bot_list = App01Botlist.objects.all()
    print(select_bot_list)
    return render(request, 'bot_list.html')
