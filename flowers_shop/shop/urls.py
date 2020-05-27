from django.urls import path
from shop.views import *


urlpatterns = [
    path('shop', ShopRender.as_view(), name='shop'),
    path('shop/<pk>', CategoryRender.as_view(), name='shop'),
    path('discount/', DiscountProducts.as_view(), name='discount'),
    path('product_detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail')
]