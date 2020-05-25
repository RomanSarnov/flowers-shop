from django.urls import path
from shop.views import abv
urlpatterns = [
    path('', abv),
]