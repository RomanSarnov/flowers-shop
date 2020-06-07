from django.urls import path
from . views import *


urlpatterns = [
    path('shop/', ProductListView.as_view(), name='shop'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('discount/', DiscountProductsView.as_view(), name='discount'),
    path('product_detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail')
]