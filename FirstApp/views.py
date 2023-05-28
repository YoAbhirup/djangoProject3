from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "FirstApp/Abhir123.html",{
        "name":"Charlie Puth"
    })
def Abhirup(request):
    return HttpResponse("Hey Abhirup")
def greet(request, name):
    return render(request, "FirstApp/Abhir123.html",{
        "name":name
    })
