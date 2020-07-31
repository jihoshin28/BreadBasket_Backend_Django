from django.db import models

# Create your models here.
class Shopper(models.Model):
    username = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    # image = models.ImageField()
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 25)
    zip_code = models.IntegerField(default = 0)
    phone = models.BigIntegerField(default = 0)
    email = models.EmailField(max_length = 100)

    def __str__(self):
        return self.name

