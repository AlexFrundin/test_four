from django.shortcuts import render

def drf_client(request):
    return render(request, 'drf_client/start.html',{})
