from django.contrib import admin
from .models import Product, Category, ProductImage

class ImageInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'available')
    inlines = (ImageInline,)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProducImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'product')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage, ProducImageAdmin)
