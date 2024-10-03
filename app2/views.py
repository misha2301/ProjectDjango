from django.shortcuts import render
from django.http import HttpResponse

def foo1(request):
    return HttpResponse("Foo 1")

def foo2(request):
    return HttpResponse("Foo 2")

def foo3(request):
    return HttpResponse("Foo 3")