from django.shortcuts import render
from django.views import View
from .forms import OrderForm


class OrderRender(View):
    def get(self, request):
        form = OrderForm()

        context = {
            'form': form
        }

        template = 'cart_order/order.html'

        return render(request, template, context)