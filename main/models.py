import datetime

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(default=datetime.date.today())
    total = models.FloatField()


class ItemOrdered(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
