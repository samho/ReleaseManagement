from django.shortcuts import render


# Create your views here.
def signin(request):
    return render(request, "login.html")


def websocket(request):
    return render(request, "websocket.html")

