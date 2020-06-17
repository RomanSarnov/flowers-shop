from django.shortcuts import render, redirect
from django.views import View
from shop.models import Product


class CartList(View):
    def get(self, request):
        if request.session.get('cart'):
            id_list = [data_dict.get('pk') for data_dict in request.session['cart'].values()]
        else:
            return render(request, 'shop/cart.html')
        cart = request.session.get('cart')
        products = Product.objects.filter(pk__in=id_list).prefetch_related('images')
        # cart = {Product.objects.get(pk=pk): item for pk, item in request.session['cart'].items()}
        for product in products:
            cart[str(product.pk)]['total_product_price'] = cart[str(product.pk)]['quantity'] * product.get_sale()
            cart[str(product.pk)]['product'] = product
        total_price = sum([item['total_product_price'] for item in cart.values()])
        print(cart)
        context = {
            'products': products,
            'cart': cart,
            'total_price': total_price
        }
        template = 'shop/cart.html'
        return render(request, template, context)


class AddToCart(View):
    def post(self, request, pk):
        if not request.session.get('cart'):
            request.session['cart'] = dict()
        else:
            request.session['cart'] = dict(request.session['cart'])
        exist = request.session['cart'].get(str(pk))
        add_data = {
            'pk': pk,
            'quantity': int(request.POST['quantity'])
        }
        if not exist:
            request.session['cart'][str(pk)] = add_data  # {pk:{}, pk:{}, pk:{}}
        else:
            item_pk = exist['pk']
            request.session['cart'][str(item_pk)]['quantity'] = request.session['cart'][str(item_pk)]['quantity'] + int(request.POST.get('quantity'))
        request.session.modified = True
        return redirect(request.POST.get('url_from'))


class RemoveFromCart(View):
    def post(self, request, pk):
        for item in list(request.session['cart'].values()):
            if item['pk'] == pk:
                print(item)
                del request.session['cart'][str(pk)]
        if not request.session.get('cart'):
            del request.session['cart']
        request.session.modified = True

        return redirect(request.POST.get('url_from'))


class DeleteCart(View):
    def post(self, request):
        del request.session['cart']

        return redirect('shop')
