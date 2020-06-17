from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderForm
from django.forms import inlineformset_factory
from customuser.models import AddressData
from orders.models import OrderItem
from shop.models import Product


class OrderCreateView(View):
    def get(self, request):
        form = OrderForm()
        context = {
            'form': form,
        }
        template = 'cart_order/order.html'

        return render(request, template, context)

    def post(self, request):
        address = AddressData.objects.create(city=request.POST.get('city'), address=request.POST.get('address'),
                                             postal_code=request.POST.get('postal_code'))
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.address = address
            order.save()
            cart = request.session.get('cart')
            products = Product.objects.filter(pk__in=cart.keys())
            for product in products:
                cart[str(product.id)]['product'] = product
            for item in cart.values():
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         quantity=item['quantity']
                                         )
            del request.session['cart']
            messages.add_message(request, messages.SUCCESS, 'Спасибо за покупку!')
        else:
            context = {
                'form': form,
            }
            template = 'cart_order/order.html'

            return render(request, template, context)
        return redirect('shop')