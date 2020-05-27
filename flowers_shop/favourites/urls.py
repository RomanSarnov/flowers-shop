from django.urls import path
from .views import AddToFavorites, RemoveFromFavorites, DeleteFavorite, FavoriteList

urlpatterns = [
   path('add/<int:pk>/', FavoriteList.as_view(), name='add_to_favourites'),
   path('remove/<int:pk>/', RemoveFromFavorites.as_view(), name='remove_from_favorites'),
   path('delete/', DeleteFavorite.as_view(), name='delete_favorites'),
   path('', FavoriteList.as_view(), name='favorite_list'),
]