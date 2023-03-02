"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import account.views
import product.views
import core.views
from product.views import ProductList, products
from account.views import register_view, signin, logout, contact
from core.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'home'), namespace='home')),
    path('account/', include(('account.urls'), namespace='account')),
    path('product/', product.views.products),
    # path('', include('account.urls')),
    path('index', account.views.index),
    path('signin', account.views.signin),
    path('logout', account.views.logout),
    path('about', account.views.about),
    path('login', account.views.register_view),
    path('contact', account.views.contact),
    path('product/list', product.views.ProductList.as_view()),
    path('product/index', account.views.index),
    path('product/signin', account.views.signin),
    path('product/logout', account.views.logout),
    path('product/about', account.views.about),
    path('product/login', account.views.register_view),
    path('product/contact', account.views.contact),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)