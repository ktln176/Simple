from django.shortcuts import render


def common_start(request):
    return render(request, 'common_start.html', {'name': 'common'})
