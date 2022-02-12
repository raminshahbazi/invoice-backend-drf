from rest_framework import serializers

from core.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "discount", "base_price", "final_price")
