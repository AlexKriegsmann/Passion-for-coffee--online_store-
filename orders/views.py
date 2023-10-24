from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from orders.models import OrderCart



@login_required
def add_to_cart(request, pk):
    product_id = pk #id-ul produsului pe care il vrem in cosul de cumparaturi
    if OrderCart.objects.filter(user_id=request.user.id, product_id=product_id, cart_item=True).exists():
        quantity =  OrderCart.objects.get(user_id=request.user.id, product_id=product_id, cart_item=True).quantity
    else:
        quantity = 1

    # verific daca produsul este in cosul de cumparaturi. daca este actualizez cantitatea
    if OrderCart.objects.filter(user_id=request.user.id, product_id=product_id, cart_item=True).exists():
       quantity += 1
       OrderCart.objects.filter(user_id=request.user.id, product_id=product_id, cart_item=True).update(quantity=quantity)
    # daca nu exista produsul in cosul de cumparaturi, il adaug
    else:
        # adaug produsul in cosul de cumparaturi
        OrderCart.objects.create(
            user_id=request.user.id,
            product_id=product_id,
            cart_item=True,
            wishlist_item=False,
            quantity=quantity,
            created_at=datetime.now()
        )

    return redirect('home_page')


def add_to_wishlist(request, pk):
    product_id = pk
    quantity = 1

    if OrderCart.objects.filter(user_id=request.user.id, product_id=product_id, wishlist_item=True).exists():
        quantity += 1
        OrderCart.objects.filter(user_id=request.user.id, product_id=product_id, wishlist_item=True).update(quantity=quantity)

    else:

        OrderCart.objects.create(
            user_id=request.user.id,
            product_id=product_id,
            cart_item=False,
            wishlist_item=True,
            quantity=quantity,
            created_at=datetime.now()
        )

    return redirect('home_page')


class CartListView(ListView):
    template_name = 'order/cart_products.html'
    model = OrderCart
    context_object_name = 'orders'

    def get_queryset(self):
        return OrderCart.objects.filter(user_id=self.request.user.id)