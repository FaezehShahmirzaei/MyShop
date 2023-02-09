from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('product/brand/', views.brand_form,name='brand'),

]