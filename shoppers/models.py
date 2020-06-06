from django.db import models

# Create your models here.
class Shopper(models.Model):
    name = models.CharField(max_length = 30)
    image = models.ImageField()
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 25)
    phone = models.IntegerField()
    email = models.EmailField(max_length = 100)
    
    def __str__(self):
        return self.name