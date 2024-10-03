from django.shortcuts import render
from django.http import HttpResponse

def func1(request):
    return HttpResponse("Это первая функция")

def func2(request):
    return HttpResponse("Это вторая функция")

def func3(request):
    return HttpResponse("Это третья функция")