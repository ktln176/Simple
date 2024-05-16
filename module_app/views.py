from django.shortcuts import render


def module_start(request):
    return render(request, 'module_start.html', {'name': 'module'})


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')
