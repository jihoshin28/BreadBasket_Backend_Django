from django.contrib import admin

# Register your models here.
from shoppers.models import Shopper, Item, Store

# class ItemInline(admin.tabularInline)

admin.site.register(Shopper)
admin.site.register(Item)
admin.site.register(Store)
