from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    return HttpResponse("View 1")

def view2(request):
    return HttpResponse("View 2")

def view3(request):
    return HttpResponse("View 3")
