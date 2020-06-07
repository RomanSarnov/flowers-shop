from django.urls import path
from .views import AddToCart, RemoveFromCart, DeleteCart, CartList


urlpatterns = [
   path('add/<int:pk>/', AddToCart.as_view(), name='add_to_cart'),
   path('remove/<int:pk>/', RemoveFromCart.as_view(), name='remove_from_cart'),
   path('delete/', DeleteCart.as_view(), name='delete_cart'),
   path('', CartList.as_view(), name='cart_list'),
]