from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=256, null=False, default="")
    discount = models.IntegerField(null=True)
    base_price = models.IntegerField()
    final_price = models.IntegerField()
    manufacturing_country = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name
