from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from core.serializers import ReadItemSerializer, WriteItemSerializer, ReadInvoiceSerializer, WriteInvoiceSerializer, \
    UserSerializer, UserInfoSerializer
# from core.permissions import IsInCanViewItems
from rest_framework.permissions import IsAuthenticated
from core.models import Item, Invoice
from rest_framework import viewsets
# import logging

# logger = logging.getLogger(__file__)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    if request.method == 'GET':
        transformer = User.objects.filter(username=request.user.username)
        serializer = UserInfoSerializer(transformer, many=True)
        return Response(serializer.data)


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'items', 'type', 'description', 'registration_date']
    
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
