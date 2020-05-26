from django.urls import path
from shop.views import *
urlpatterns = [
    path('', abv),
    path('product_list', ProductList.as_view())
]