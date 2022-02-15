from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Item, Invoice, InvoiceType, Country


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceType
        fields = ("id", "name")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name",)


class WriteItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Item
        fields = ("user", "name", "discount", "base_price", "final_price", "manufacturing_country")


class ReadItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    manufacturing_country = CountrySerializer()

    class Meta:
        model = Item
        fields = ("id", "user", "name", "discount", "base_price", "final_price", "manufacturing_country")
        read_only_fields = fields


class WriteInvoiceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Invoice
        fields = ("user", "date", "items", "type", "description")

    def create(self, validated_data):
        items = validated_data.pop("items")
        user_owns_items_only = list(filter(lambda x: x.user == self.context["request"].user, items))
        invoice = Invoice.objects.create(**validated_data)
        for i in user_owns_items_only:
            invoice.items.add(i.id)
        return invoice


class ReadInvoiceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items = ReadItemSerializer(many=True, read_only=True)
    type = TypeSerializer()

    class Meta:
        model = Invoice
        fields = ("user", "date", "items", "type", "description", "registration_date")
        read_only_fields = fields
