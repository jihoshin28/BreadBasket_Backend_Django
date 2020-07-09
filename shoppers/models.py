from django.db import models

# Create your models here.
class Shopper(models.Model):
    name = models.CharField(max_length = 30)
    # image = models.ImageField()
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 25)
    phone = models.IntegerField()
    email = models.EmailField(max_length = 100)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 25)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    shopper = models.ForeignKey(Shopper, on_delete = models.CASCADE)
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    item = models.ManytoManyField(Item)

class Item(models.Model):
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    shopper = models.ForeignKey(Shopper, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    # image = models.ImageField()
    
    def __str__(self):
        return self.name




