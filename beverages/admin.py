from django.contrib import admin

# Register your models here.
from .models import (
    BeverageType,
    Beverage,
    # Ingredients,
    # Recipe,
)

admin.site.register(Beverage)
admin.site.register(BeverageType)
# admin.site.register(Ingredients)
# admin.site.register(Recipe)
