# Generated by Django 4.0.2 on 2022-02-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_item_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='base_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='final_price',
            field=models.IntegerField(null=True),
        ),
    ]