from django.shortcuts import render


def core_start(request):
    return render(request, 'core_start.html', {'name': 'core'})


def home(request):
    return render(request, 'home.html')
