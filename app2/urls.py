from django.urls import path
from . import views

urlpatterns = [
    path('foo1/', views.foo1, name='foo'),
    path('foo2/', views.foo2, name='foo2'),
    path('foo3/', views.foo3, name='foo3'),
]
