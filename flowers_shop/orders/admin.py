from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email',
                    'address', 'paid',
                    'created', 'updated')
    list_filter = ('paid', 'created', 'updated')
    inlines = [OrderItemInline]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product')
    list_display_links = ('order', 'product')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)