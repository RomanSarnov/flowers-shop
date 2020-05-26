from django.urls import path
from shop.views import *
urlpatterns = [
    path('product_list', ProductList.as_view(), name='product_list'),
    path('discount/', DiscountProducts.as_view(), name='discount')
]