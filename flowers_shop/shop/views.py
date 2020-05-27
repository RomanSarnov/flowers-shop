from django.shortcuts import render
from django.views import View
from .models import ProductImage, Product, Category
import requests


class ProductList(View):
    def get(self,request):
        products = Product.objects.filter(available=True)
        return render(request, 'shop/shop.html', context={'products': products})


class DiscountProducts(View):
    def get(self, request):
        products = Product.objects.filter(stock__gt=0)
        return render(request, 'shop/discount.html', context={'products': products})
