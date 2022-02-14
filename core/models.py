from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Country(models.Model):
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return str(self.name)


class InvoiceType(models.Model):
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=False, default="")
    discount = models.IntegerField()
    base_price = models.IntegerField()
    final_price = models.IntegerField()
    manufacturing_country = models.ForeignKey(to=Country, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} -" \
               f" {self.discount} -" \
               f" {self.base_price} -" \
               f" {self.final_price} -" \
               f" {self.final_price} -" \
               f" {self.manufacturing_country} "


class Invoice(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, default=datetime.now)
    items = models.ManyToManyField(Item)
    type = models.ForeignKey(to=InvoiceType, null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    registration_date = models.DateField(null=False, default=datetime.now)

    def __str__(self):
        return f"{self.user} - {self.type} - {self.description}"


class InvoiceChangeLog(models.Model):
    base_invoice = models.ForeignKey(to=Invoice, on_delete=models.CASCADE)
    last_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    last_items = models.ManyToManyField(Item)
    last_type = models.ForeignKey(to=InvoiceType, null=True, on_delete=models.CASCADE)
    last_description = models.TextField(null=True)
    last_date = models.DateField(null=False, default=datetime.now)
    last_registration_date = models.DateField(null=False, default=datetime.now)
    change_date = models.DateField(null=False, default=datetime.now)
