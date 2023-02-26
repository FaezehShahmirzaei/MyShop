from django.contrib import admin
from django.urls import path, include

import product.views
from . import views
from .views import ProductList,products

urlpatterns = [
    # path('list', ProductList.as_view()),
    # path('', product.views.products),

    # path('brand/', BrandListView.as_view(), name='brand_list'),
]
