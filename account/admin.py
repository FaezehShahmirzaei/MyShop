from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account, AccountAddress, City, State, OtpCode
from .form import UserCreationForm, UserChangeForm

"""
setting Account fields to show in admin Panel
"""


class AccountAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        'email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_customer',
        'is_superuser', 'gender', 'password',)
    fieldsets = (
        ('main', {'fields': ('email', 'username', 'date_joined', 'last_login', 'gender', 'password',)}),
        ('permission', {'fields': ('is_admin', 'is_active', 'is_staff', 'is_customer', 'is_superuser')}),
    )
    # add_fieldsets = ('change', {'email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active',
    #                             'is_staff', 'is_customer', 'is_superuser', 'gender', 'password', })

    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ('is_admin',)
    ordering = ('username',)


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created',)


class StateAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('name',)


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', ]
    search_fields = ('name', 'state',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ('state',)
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
# admin.site.register(OtpCode, OtpCodeAdmin)
