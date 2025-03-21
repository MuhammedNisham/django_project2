from django.contrib import admin

#importing neccessary models

from .models import Product

# Register your models here.
# Every model registered here, will  be available in django prebuilt admin panel
admin.site.register(Product)