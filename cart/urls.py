
from django.contrib import admin
from django.urls import path,include
from .view import cartpage

urlpatterns = [
    path(" ",cartpage),
]
