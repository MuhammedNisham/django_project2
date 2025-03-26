from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

from django.views.generic import DetailView

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