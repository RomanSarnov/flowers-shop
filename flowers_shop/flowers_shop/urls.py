from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf .urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('favourites/', include('favourites.urls')),
    path('cart', include('cart.urls')),
    path('orders', include('order.urls')),
    path('user/', include('customuser.urls')),
    path('contact/', include('contact.urls'))
]
# Для обнаружения медиа файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)