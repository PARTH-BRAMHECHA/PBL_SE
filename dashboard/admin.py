from django.contrib import admin
from .models import Product
from .models import Order
from django.contrib.auth.models import Group
# Register your models here.
admin.site.site_header = 'KenInventory Dashboard'

class ProductAdim(admin.ModelAdmin):
    list_display=('name','category','quantity')
    list_filter=['category',]

admin.site.register(Product,ProductAdim)
admin.site.register(Order,)
#admin.site.unregister(Group)