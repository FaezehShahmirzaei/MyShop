from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Discount, Product
#
# """
# setting Category fields to show in admin Panel
# """
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name', )
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()


admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Discount)
