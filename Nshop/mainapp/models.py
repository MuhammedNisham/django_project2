from django.db import models

# Create your models here.
# every class defined here


class Product(models.Model):
    #id will be automatically created by django
    name = models.CharField(max_length=255)
    price = models.FloatField()
    desc = models.TextField(max_length=500)
    img = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()

