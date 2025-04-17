from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    name = "ryad"
    return HttpResponse(f"<h1 style='color:chartreuse'>Hello {name}</h1>")