from django.contrib import admin

# Register your models here.
from drivers.models import Driver

# class ItemInline(admin.tabularInline)

admin.site.register(Driver)

