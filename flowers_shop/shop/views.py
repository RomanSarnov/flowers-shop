from django.shortcuts import render
from django.views import View
from .models import ProductImage, Product, Category

def abv(request):
    return render(request, 'shop/index.html')


class ProductList(View):
    def get(self,request):
        products = Product.objects.filter(available=True)
        return render(request, 'shop/shop.html', context={'products': products})