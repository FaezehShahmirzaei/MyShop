from django.contrib import admin

# Register your models here.
from .models import Order,OrderDetail,Cart

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)