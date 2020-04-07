from .views import HelloWorld, index
from django.urls import path

urlpatterns = [
    path('hello/', HelloWorld),
    path('index/', index)
]