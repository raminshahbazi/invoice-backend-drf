from core.serializers import ItemSerializer, InvoiceSerializer
# from core.permissions import IsInCanViewItems
from rest_framework.permissions import IsAuthenticated
from core.models import Item, Invoice
from rest_framework import viewsets


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)
