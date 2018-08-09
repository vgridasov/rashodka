from django.contrib import admin

# Register your models here.
from .models import Cat, Vendor, Ware, Seller, Price

admin.site.register(Cat)
admin.site.register(Vendor)
admin.site.register(Ware)
admin.site.register(Seller)
admin.site.register(Price)

