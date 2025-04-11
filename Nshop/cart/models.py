from django.db import models

from mainapp.models import Product

from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    user = models.ForeignKey(User, on_delete= models.CASCADE)

    quantity = models.IntegerField(default=0)

    date_added = models.DateTimeField(auto_now_add=True)
    #for current time stamp

    def __str__(self):
        return f"{self.product.name} added by {self.user.username} at {self.date_added}"