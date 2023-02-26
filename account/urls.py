from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index, signin

app_name='account'
urlpatterns = [
    path('', views.index),
    path('register/',views.UserRegisterView.as_view(), name='user_register'),
    path('verify/',views.UserRegistrationVerifyCodeView.as_view(), name='verify_code'),


 ]
