from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category



# Render shop page
class ShopRender(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        categories = Category.objects.all()

        context = {
            'products': products,
            'categories': categories,
        }
        template = 'shop/shop.html'

        return render(request, template, context)


# Render category page
class CategoryRender(View):
    def get(self, request, pk):
        products = Product.objects.filter(available=True)
        categories = Category.objects.all()

        context = {
            'products': products,
            'categories': categories,
        }
        template = 'shop/category.html'

        return render(request, template, context)


class DiscountProducts(View):
    def get(self, request):
        products = Product.objects.filter(stock__gt=0)
        return render(request, 'shop/discount.html', context={'products': products})

class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        first_product_image = product.images.first()
        product_images = product.images.all()[1:]
        return render(request, 'shop/product_detail.html', context={'product': product, 'product_images': product_images, 'first_product_image': first_product_image})
