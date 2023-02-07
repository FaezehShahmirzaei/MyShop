from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import Account, AccountAddress, City, State


# Register your models here.
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


admin.site.register(Account, AccountAdmin)
admin.site.register(AccountAddress)
admin.site.register(City)
admin.site.register(State)