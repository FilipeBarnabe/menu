from __future__ import annotations
from django.db import models


def get_new_default() -> int:
    try:
        return (
            BeverageType.objects.all().aggregate(models.Max("order"))["order__max"] + 1
        )
    except:
        return 1


# Create your models here.
class BeverageType(models.Model):
    type_name = models.CharField(max_length=20)
    type_icon = models.CharField(max_length=50, default="fa-glass-cheers")
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self) -> str:
        return self.type_name


def upload_name(instance: Beverage, filename: str) -> str:
    _, extension = filename.split(".")
    return f"beverages/{instance.name}_{instance.id}_{instance.beverage_type.id}.{extension}"


class Beverage(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    post_link = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=upload_name, blank=True)
    beverage_type = models.ForeignKey(BeverageType, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
