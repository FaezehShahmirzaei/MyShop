from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.

def brand_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        c = models.Brand()
        c.name=name
        c.save()
    return render(request,'brad/brand.html')