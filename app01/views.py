from django.http import HttpResponse


# Create your views here.

def demo(request):
    return HttpResponse('Demo')


def home(request):
    return HttpResponse('Home')


def start(request):
    return HttpResponse('Start')
