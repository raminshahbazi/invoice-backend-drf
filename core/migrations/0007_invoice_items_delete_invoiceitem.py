# Generated by Django 4.0.2 on 2022-02-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_invoiceitem_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='items',
            field=models.ManyToManyField(to='core.Item'),
        ),
        migrations.DeleteModel(
            name='InvoiceItem',
        ),
    ]
