from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from shop.models import Product

class FavoriteList(View):
    def get(self, request):
        if request.session['favorites']:
            id_list = [data_dict.get('pk') for data_dict in request.session['favorites']]
            print(id_list)
        else:
            print('fdsggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg')
        products = Product.objects.filter(pk__in = id_list)
        return render(request, 'shop/favorites.html', context={'products': products})

class AddToFavorites(View):
    def get(self, request, pk):
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
        a = request.session['favorites']
        request.session.modified = True
        return HttpResponse(f'<h1>gfdgdfg</h1>{request.session["favorites"]}')


class RemoveFromFavorites(View):
    def get(self, request, pk):
        for item in request.session['favorites']:
            if item['pk'] == pk:
                item.clear()
        request.session.modified = True
        while {} in request.session['favorites']:
            request.session['favorites'].remove({})
        request.session.modified = True
        return HttpResponse(f'<h1>gfdgdfg</h1>{request.session["favorites"]}')


class DeleteFavorite(View):
    def get(self, request):
        del request.session['favorites']
