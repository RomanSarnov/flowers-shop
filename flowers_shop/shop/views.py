from django.shortcuts import render
from django.views import View
from .models import Product, Category
import requests


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
    def get(self, request):
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
