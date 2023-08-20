from django.contrib import admin

# Register your models here.
from .models import BeverageType, Beverage

admin.site.register(Beverage)
admin.site.register(BeverageType)
