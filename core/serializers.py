from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Item, Invoice, InvoiceType, Country, InvoiceChangeLog


# todo: consider combine UserInfoSerializer and UserSerializer together
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


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

    def update(self, instance, validated_data):
        icl = InvoiceChangeLog.objects.create(
            base_invoice=instance,
            last_user=instance.user,
            last_type=instance.type,
            last_description=instance.description,
            last_date=instance.date,
            last_registration_date=instance.registration_date
        )
        for i in instance.items.all():
            icl.last_items.add(i.id)
        icl.save()

        instance.description = validated_data.get('description', instance.description)
        instance.type = validated_data.get('type', instance.type)
        instance.date = validated_data.get('date', instance.date)
        instance.items.clear()

        items = validated_data.pop("items")
        user_owns_items_only = list(filter(lambda x: x.user == self.context["request"].user, items))
        for i in user_owns_items_only:
            instance.items.add(i.id)
        return instance


class ReadInvoiceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items = ReadItemSerializer(many=True, read_only=True)
    type = TypeSerializer()

    class Meta:
        model = Invoice
        fields = ("user", "date", "items", "type", "description", "registration_date")
        read_only_fields = fields
