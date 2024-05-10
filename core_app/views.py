from django.shortcuts import render


def core_start(request):
    return render(request, 'core_start.html', {'name': 'core'})
