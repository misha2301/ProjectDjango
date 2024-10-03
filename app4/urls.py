from django.urls import path
from . import views

urlpatterns = [
    path('f1/', views.f1, name='f1'),
    path('f2/', views.f2, name='f2'),
    path('f3/', views.f3, name='f3'),
]