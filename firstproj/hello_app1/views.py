from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request) :
    #return HttpResponse("Hello")
    return render(request, "hello/index.html")

def rai(request) :
    return HttpResponse("Hello Rai")

def greet(request, name) :
    #return HttpResponse(f"Hello, {name.upper()}")
    return render(request, "hello/greet.html", {
        "name" : name.upper()
    })
