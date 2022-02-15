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
        # read_only_fields = fields


class WriteInvoiceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # items = ReadItemSerializer(many=True)
    type = TypeSerializer()

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['type'] = ReadItemSerializer(instance.type).data
    #     return ret

    class Meta:
        model = Invoice
        fields = ("user", "date", "items", "type", "description")

    def create(self, validated_data):
        # todo : check accept only users owns items
        typee = validated_data.pop('type')
        itemss = validated_data.pop('items')
        print(typee)
        print(itemss)
        print(validated_data)
        invoice = Invoice.objects.create(**validated_data)
        invoice.items.add(itemss[0].id)
        print(invoice)
        print("_________________________")
        print(self.context["request"].user)
        # items = validated_data.pop('items')
        # type2 = validated_data.pop('type')
        # instance = Invoice.objects.create(**validated_data)
        # instance.items = items
        # instance.type = type2
        raise serializers.ValidationError("human readable error message here")

        # except (True):
        #     raise serializers.ValidationError("human readable error message here")
        # return invoice

    def update(self, instance, validated_data):
        return
        # todo : check accept only users owns items

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context["request"].user
        self.fields["items"].queryset = Item.objects.filter(user=user)


class ReadInvoiceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items = ReadItemSerializer(many=True, read_only=True)
    type = TypeSerializer()

    class Meta:
        model = Invoice
        fields = ("user", "date", "items", "type", "description", "registration_date")
        read_only_fields = fields
