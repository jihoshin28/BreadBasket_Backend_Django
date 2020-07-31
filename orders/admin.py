from django.contrib import admin

# Register your models here.
from orders.models import Store, Item, Order

# class ItemInline(admin.tabularInline)

admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Order)


