from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Item, Invoice, InvoiceItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "discount", "base_price", "final_price")


class InvoiceItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = InvoiceItem
        fields = ("invoice", "item", "registration_date")


class InvoiceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    invoice_items = serializers.StringRelatedField(many=True)
    # invoice_items = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='invoice_items'
    #  )

    class Meta:
        model = Invoice
        fields = ("user", "date", "type", "description", "registration_date", "invoice_items")
