from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from shop.models import Product


class FavoriteList(View):
    def get(self, request):
        if request.session.get('favorites'):
            id_list = [data_dict.get('pk') for data_dict in request.session['favorites']]
        else:

            return render(request, 'shop/favorites.html')
        products = Product.objects.filter(pk__in = id_list)
        return render(request, 'shop/favorites.html', context={'products': products})

class AddToFavorites(View):
    def post(self, request, pk):
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])
        add_data = {
            'pk': pk
        }
        exist = [True for item in request.session['favorites'] if item['pk'] == pk]
        if not exist:
            request.session['favorites'].append(add_data)  # [{}, {}, {}]
        request.session.modified = True
        print(request.POST.get('url_from'))
        return redirect(request.POST.get('url_from'))


class RemoveFromFavorites(View):
    def post(self, request, pk):
        for item in request.session['favorites']:
            if item['pk'] == pk:
                request.session['favorites'].remove(item)
        if not request.session.get('favorites'):
            del request.session['favorites']
        request.session.modified = True

        return redirect(request.POST.get('url_from'))


class DeleteFavorite(View):
    def post(self, request):
        del request.session['favorites']
        return redirect('shop')