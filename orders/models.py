from django.db import models
from drivers.models import *
from shoppers.models import *
# Create your models here.
class Order(models.Model):
    order_driver = models.ForeignKey(Driver, on_delete= models.PROTECT)
    order_shopper = models.ForeignKey(Shopper, on_delete= models.PROTECT)

    def __str__(self):
        return self.name

