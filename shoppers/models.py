from django.db import models
from django.utils import timezone

# Create your models here.
class Shopper(models.Model):
    username = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    # image = models.ImageField()
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 25)
    zip_code = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.EmailField(max_length = 100)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 25)
    phone = models.BigIntegerField()
    
    def __str__(self):
        return self.name
        
class Item(models.Model):
    name = models.CharField(max_length = 50)
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    found = models.BooleanField(default = False)
    quantity_unit = models.CharField(default = "items", max_length = 15)
    quantity_number = models.BigIntegerField(default = 1)
    price = models.FloatField(default = 0)
    # image = models.ImageField()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    shopper = models.ForeignKey(Shopper, related_name = "shopper", on_delete = models.CASCADE)
    items = models.ManyToManyField(Item)
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    created_at = models.DateTimeField('created date')
    total = models.BooleanField(default = 0)
    payment = models.BooleanField(default = 0)
    status = models.CharField(max_length = 50, default = "active")

    def __str__(self):
        return self.shopper.name

