
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(default=timezone.now)
    total = models.FloatField()

    def __str__(self):
        return "Order no. {} for {}".format(self.id, self.user.username)


class ItemOrdered(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def __str__(self):
        return "Item in order no. {}".format(self.order_id)
