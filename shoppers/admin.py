from django.contrib import admin

# Register your models here.
from shoppers.models import Shopper

# class ItemInline(admin.tabularInline)

admin.site.register(Shopper)

