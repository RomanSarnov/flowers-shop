from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category
from cart.forms import CartAddProductForm


# Render shop page
class ProductListView(View):
    def get(self, request):
        products = Product.objects.filter(available=True).prefetch_related('images')
        categories = Category.objects.all()
        form = CartAddProductForm()
        context = {
            'products': products,
            'categories': categories,
            'form': form
        }
        template = 'shop/shop.html'
        return render(request, template, context)

    def get_first(self, queryset):
        return queryset[0]


# Render category page
class CategoryDetailView(View):
    def get(self, request, slug):
        products = Product.objects.filter(category__slug=slug, available=True)\
            .select_related('category')\
            .prefetch_related('images')
        categories = Category.objects.all()

        context = {
            'products': products,
            'categories': categories,
        }
        template = 'shop/category.html'

        return render(request, template, context)


class DiscountProductsView(View):
    def get(self, request):
        products = Product.objects.filter(stock__gt=0).prefetch_related('images')

        context = {
            'products': products
        }
        template = 'shop/discount.html'

        return render(request, template, context)


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        first_product_image = product.images.first()
        product_images = product.images.all()[1:]

        context = {
            'product': product,
            'product_images': product_images,
            'first_product_image': first_product_image
        }
        template = 'shop/product_detail.html'

        return render(request, template, context)
