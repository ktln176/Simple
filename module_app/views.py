from django.shortcuts import render


def module_start(request):
    return render(request, 'module_start.html', {'name': 'module'})
