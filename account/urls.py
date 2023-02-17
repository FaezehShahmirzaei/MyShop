from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index, signin

urlpatterns = [
    path('', views.index),
 ]
