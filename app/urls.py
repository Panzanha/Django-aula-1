from .views import HelloWorld, index, base
from django.urls import path

urlpatterns = [
    path('hello/', HelloWorld),
    path('index/', index),
    path('base/', base),
]