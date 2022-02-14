from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Item, Invoice
from core.permissions import IsInCanViewItems
from core.serializers import ItemSerializer, InvoiceSerializer


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()


class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.all()


class Test(APIView):
    permission_classes = [IsAuthenticated, IsInCanViewItems]

    def get(self, request):
        return Response({"a": "a", "user": request.user.username})
