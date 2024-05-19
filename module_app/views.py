from django.middleware.csrf import get_token
from django.shortcuts import render


def module_start(request):
    return render(request, 'module_start.html', {'name': 'module'})


def login(request):
    print(request)
    return render(request, 'login.html')


def sign(request):
    csrf_token = get_token(request)
    result_dict = {'csrf_token': csrf_token}
    return render(request, 'sign.html', result_dict)
