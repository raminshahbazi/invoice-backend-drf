from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Invoice(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, default=datetime.now)

    class YearInSchool(models.TextChoices):
        TYPE1 = 'T1', _('Type 1')
        TYPE2 = 'T2', _('Type 2')
        TYPE3 = 'T3', _('Type 3')
    type = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.TYPE1,
    )
    description = models.TextField(null=True)
    registration_date = models.DateField(null=False, default=datetime.now)

    def __str__(self):
        return f"{self.user} - {self.type} - {self.description}"


class Item(models.Model):
    name = models.CharField(max_length=256, null=False, default="")
    discount = models.IntegerField()
    base_price = models.IntegerField()
    final_price = models.IntegerField()
    manufacturing_country = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(to=Invoice, on_delete=models.CASCADE)
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    registration_date = models.DateField(null=False, default=datetime.now)

    def __str__(self):
        return f"{self.invoice} - {self.item} - {self.registration_date}"

