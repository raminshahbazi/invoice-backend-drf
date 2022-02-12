from rest_framework.generics import ListAPIView
from core.models import Item
from core.serializers import ItemSerializer


class ItemListAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
