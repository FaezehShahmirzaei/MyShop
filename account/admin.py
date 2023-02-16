from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import Account, AccountAddress, City, State

"""
setting Account fields to show in admin Panel
"""


class AccountAdmin(UserAdmin):
    list_display = (
        'email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_customer',
        'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class StateAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', ]
    search_fields = ('name', 'state',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class AccountAddressAdmin(admin.ModelAdmin):
    list_display = ['account', 'city', 'address', 'postalcode', 'receiver_mobile', ]
    search_fields = ('account', 'city', 'address', 'postalcode', 'receiver_mobile',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(Account, AccountAdmin)
admin.site.register(AccountAddress, AccountAddressAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
