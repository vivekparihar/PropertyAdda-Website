from django.contrib import admin
from .models import forSale, forRent, sellers
# Register your models here.

admin.site.register(forSale)
admin.site.register(forRent)
admin.site.register(sellers)

