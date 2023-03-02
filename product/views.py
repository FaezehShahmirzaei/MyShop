from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Brand, Product


class ProductList(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs


class ProductDetail(DetailView):
    model = Product


def products(request):
    return render(request,'products.html')