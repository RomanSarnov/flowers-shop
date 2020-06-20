from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf .urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('favourites/', include('favourites.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('user/', include('customuser.urls')),
    path('contact/', include('contact.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

# Для обнаружения медиа файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns