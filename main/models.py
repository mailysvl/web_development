
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=15)
    address = models.CharField(max_length=100)


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name, self.price


class Order(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(default=timezone.now)
    total = models.FloatField()


class ItemOrdered(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
