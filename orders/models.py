from django.db import models
from drivers.models import Driver
from shoppers.models import Shopper
from django.utils import timezone

# Create your models here.

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
    price = models.FloatField(default = 0)
    # image = models.ImageField()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    order_driver = models.ForeignKey(Driver, on_delete= models.CASCADE)
    order_shopper = models.ForeignKey(Shopper, on_delete= models.CASCADE)
    items = models.ManyToManyField(Item)
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    created_at = models.DateTimeField('created date')
    total = models.BooleanField(default = 0)
    payment = models.BooleanField(default = 0)
    distance = models.IntegerField(default = 0)
    units = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name


        
