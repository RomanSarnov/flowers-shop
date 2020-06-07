from django.shortcuts import render, redirect
from django.views import View
from shop.models import Product


class CartList(View):
    def get(self, request):
        if request.session.get('cart'):
            id_list = [data_dict.get('pk') for data_dict in request.session['cart']]
        else:
            return render(request, 'shop/cart.html')

        products = Product.objects.filter(pk__in=id_list)

        context = {
            'products': products
        }
        template = 'shop/cart.html'

        return render(request, template, context)


class AddToCart(View):
    def post(self, request, pk):
        if not request.session.get('cart'):
            request.session['cart'] = list()
        else:
            request.session['cart'] = list(request.session['cart'])

        exist = [True for item in request.session['cart'] if item['pk'] == pk]

        add_data = {
            'pk': pk
        }

        if not exist:
            request.session['cart'].append(add_data)  # [{}, {}, {}]
        request.session.modified = True
        print(request.POST.get('url_from'))

        return redirect(request.POST.get('url_from'))


class RemoveFromCart(View):
    def post(self, request, pk):
        for item in request.session['cart']:
            if item['pk'] == pk:
                request.session['cart'].remove(item)
        if not request.session.get('cart'):
            del request.session['cart']
        request.session.modified = True

        return redirect(request.POST.get('url_from'))


class DeleteCart(View):
    def post(self, request):
        del request.session['cart']

        return redirect('shop')


class GetOrder(View):
    pass