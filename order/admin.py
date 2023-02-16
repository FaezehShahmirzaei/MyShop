from django.contrib import admin

from .models import Order, OrderDetail, Cart


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','mobile' ,'insert_date','receive_date','status','cart']
    search_fields = ('customer','mobile','insert_date','receive_date','status','cart')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order', 'product','count','price',]
    search_fields = ('order','product','count','price')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CartAdmin(admin.ModelAdmin):
    list_display = ['code','price' ]
    search_fields = ('code','price')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Cart, CartAdmin)
