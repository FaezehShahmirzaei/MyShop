from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ProductList, index

urlpatterns = [
    path('', views.index, name='index'),
    path('list', ProductList.as_view()),

    # path('brand/', BrandListView.as_view(), name='brand_list'),
]
