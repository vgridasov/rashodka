from django.contrib import admin

# Register your models here.
from .models import Ware, Seller, Price

admin.site.register(Ware)
admin.site.register(Seller)
admin.site.register(Price)

