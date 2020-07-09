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
        
class Item(models.Model):
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    price = models.FloatField()
    # image = models.ImageField()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    shopper = models.ForeignKey(Shopper, related_name = "shopper", on_delete = models.CASCADE)
    items = models.ManyToManyField(Item)
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    

    def __id__(self):
        return self.id

    def __str__(self):
        return self.name






