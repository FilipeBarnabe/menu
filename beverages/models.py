from django.db import models


# Create your models here.
class BeverageType(models.Model):
    type_name = models.CharField(max_length=20)

    class Meta:
        ordering = ["type_name"]

    def __str__(self) -> str:
        return self.type_name


class Beverage(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link = models.CharField(max_length=255, blank=True)
    beverage_type = models.ForeignKey(BeverageType, on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
