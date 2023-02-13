from django.contrib import admin
from django.urls import path, include
from .views import ProductList

urlpatterns = [
    path('',ProductList.as_view()),

    # path('brand/', BrandListView.as_view(), name='brand_list'),
]