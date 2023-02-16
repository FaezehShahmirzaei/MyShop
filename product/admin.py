from django.contrib import admin

# Register your models here.
from product.models import Brand, Category, Discount, Product


#
# """
# setting Category fields to show in admin Panel
# """
#
#
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'status']
    search_fields = ('name', 'price')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'amount', 'is_active','discount_limit']
    search_fields = ('name', 'status','amount', 'is_active','discount_limit')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
