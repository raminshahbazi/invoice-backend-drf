from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Item, Invoice


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class ItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Item
        fields = ("id", "user", "name", "discount", "base_price", "final_price")


class InvoiceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ("user", "date", "items", "type", "description", "registration_date")
