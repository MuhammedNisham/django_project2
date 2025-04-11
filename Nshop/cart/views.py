from django.shortcuts import render, redirect
from django.template import loader
from .models import CartItem
from mainapp.models import Product
 
 
 # Create your views here
 
def viewCart(request):
    cartItems = CartItem.objects.filter(user = request.user)
 
    template = 'cart.html'
 
    context = {
       'items' : cartItems
    }
 
    return render(request, template, context)

def addToCart(request, product_id):

    this_product = Product.objects.get(id = product_id)
    cart_item, created_at = CartItem.objects.get_or_create(product = this_product, user = request.user)
    cart_item.quantity += 1

    cart_item.save()
    return redirect('view_cart')
