from rest_framework.response import Response

from core.serializers import ReadItemSerializer, WriteItemSerializer, ReadInvoiceSerializer , WriteInvoiceSerializer
# from core.permissions import IsInCanViewItems
from rest_framework.permissions import IsAuthenticated
from core.models import Item, Invoice
from rest_framework import viewsets
# import logging

# logger = logging.getLogger(__file__)


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadItemSerializer
        return WriteItemSerializer

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadInvoiceSerializer
        return WriteInvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)


# class Test(viewsets.ModelViewSet):
#
#     def get_queryset(self):
#         return Invoice.objects.filter(user=self.request.user)
#
#     def list(self, request, *args, **kwargs):
#         logger.error("++++++++++++++This logs an info message.")
#         logger.debug("___________________________debug_________________")
#         logger.info("___________________________info_________________")
#         logger.warning("___________________________warning_________________")
#         return Response({"user": request.user.id})
