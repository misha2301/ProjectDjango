from django.shortcuts import render
from django.http import HttpResponse

def f1(request):
    return HttpResponse("Первая функция представления")

def f2(request):
    return HttpResponse("Вторая функция представления")

def f3(request):
    return HttpResponse("Третья функция представления")

