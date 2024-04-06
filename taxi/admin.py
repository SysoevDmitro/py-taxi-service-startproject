from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Manufacturer, Driver, Car


class DriverAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional info", {"fields": ("driver_license", "phone_number")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "driver_license", "phone_number"),
        }),
    )
    search_fields = ("username", "email", "driver_license", "phone_number")
    ordering = ("username",)
    filter_horizontal = ("groups", "user_permissions",)


class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer"]


# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
