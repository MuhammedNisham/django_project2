from django.shortcuts import render, redirect
from django.template import loader
from .models import CartItem
from mainapp.models import Product
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.shortcuts import get_list_or_404
 
 
 # Create your views here

@login_required
def viewCart(request):
    cartItems = CartItem.objects.filter(user = request.user)

    total_price = sum([float(item.product.price) * item.quantity for item in cartItems])
 
    template = 'cart.html'
 
    context = {
       'items' : cartItems,
       'total' : total_price
    }
 
    return render(request, template, context)

@login_required
def addToCart(request, product_id):

    this_product = Product.objects.get(id = product_id)
    cart_item, created_at = CartItem.objects.get_or_create(product = this_product, user = request.user)
    cart_item.quantity += 1

    cart_item.save()
    return redirect('view_cart')

@login_required
def remFromCart(request,cart_item_id):
    this_cart_item = CartItem.objects.get(id = cart_item_id)
    this_cart_item.delete() # this will delete the cart_item_object and its associated record in the CartItem table in db
 
    return redirect('view_cart')
#this is a api function
@login_required
def addQuantity(request, cart_item_id):
    cart_item = get_list_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    overall_total = sum(item.get_total() for item in CartItem.objects.filter(user=request.user))
    context = {
        'quantity': cart_item.quantity,
        'total_price': cart_item.get_total(),
        'overall_total': overall_total
        }
    return JsonResponse(context)

@login_required
def remQuantity(request, cart_item_id):
    cart_item = get_list_or_404(CartItem, id=cart_item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        overall_total = sum(item.get_total() for item in CartItem.objects.filter(user=request.user))
        context = {
            'quantity' : cart_item.quantity,
            'total_price': cart_item.get_total(),
            'overall_total': overall_total
        }
        return JsonResponse(context)
    else:
        cart_item.delete()
        overall_total = sum(item.get_total() for item  in CartItem.objects.filter(user=request.user))
        context = {
            'quantity': 0,
            'total_price': 0,
            'overall_total': overall_total
        }
        return JsonResponse(context)