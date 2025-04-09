from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

from django.views.generic import DetailView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product
# Create your views here.
def homeView(request):
    #template
    template = loader.get_template('home.html')

    # context data
    context = {
        'products' : Product.objects.all()

    }
    return HttpResponse(template.render(context, request))

class ProductDetails(DetailView):
    model = Product
    template_name = 'product_details.html'


def aboutView(request):
    template = loader.get_template('about.html')

    context = {

    }
    return HttpResponse(template.render(context, request))

def ContactView(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))

class AddProduct(CreateView):
     model = Product
     template_name = 'add_products.html'
     fields = '__all__' # include all the fields in the form
     # This view on successful addition of products, redirects the user to a 
     # new page, to set this page, we do the below line of code
     success_url = '/'

class EditProduct(UpdateView):
     model = Product
     context_object_name = 'product'
     template_name = 'edit_product.html'
     fields = ['img','price', 'stock', 'desc']
     success_url = '/'

class DelProduct(DeleteView):
     model = Product
     template_name = 'del_product.html'
     success_url = '/'