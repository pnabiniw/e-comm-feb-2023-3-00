import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        order = {"get_cart_items": 0, "get_cart_total": 0, "shipping": False}
        items = []
        cart_items = order['get_cart_items']
    context = {"products": Product.objects.all(), "cart_items": cart_items}
    print(context)
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        order = {"get_cart_items": 0, "get_cart_total": 0}
        items = []
        cart_items = order['get_cart_items']
    context = {"items": items, "order": order, "cart_items": cart_items, "shipping": False}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        order = {"get_cart_items": 0, "get_cart_total": 0}
        items = []
        cart_items = order['get_cart_items']
    context = {"items": items, "order": order, "cart_items": cart_items, "shipping": False}
    return render(request, 'store/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1
    order_item.save()
    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse("Working", safe=False)
