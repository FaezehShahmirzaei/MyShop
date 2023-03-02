from django.shortcuts import render , get_object_or_404
from django.views import View
from product.models import Product


# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'home.html', {'product': products})
# return render(request, 'home.html')

class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, "detail.html", {'product': product})