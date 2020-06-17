from django.contrib import admin
from .models import CustomUser, AddressData


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('username', )

class AddressDataAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'postal_code')
    list_display_links = ('address', )


admin.site.register(CustomUser, UserAdmin)
admin.site.register(AddressData, AddressDataAdmin)