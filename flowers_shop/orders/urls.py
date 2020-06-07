from django.urls import path
from .views import *


urlpatterns = [
    path('order/', UserCreateView.as_view(), name='register'),

]