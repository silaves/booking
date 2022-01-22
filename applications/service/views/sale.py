from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.service.models.sale import Sale
from applications.service.models.booking import Booking
from applications.service.models.invoice import Invoice
from .support import *


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ['status', 'nit', 'total']


class SaleView(APIView, SerializingSupportMixin):
    permission_classes = []
    request_serializer = SaleSerializer

    def post(self, request: Request, pk: int):
        try:
            sale = Sale.objects.get(pk=pk)
            booking = Booking.objects.get(sale=sale)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if booking.status == Booking.PAID:
            sale.status = Sale.FINISHED
            sale.save()
            invoice = Invoice()
            invoice.nit = booking.client.nit
            invoice.client = booking.client.name
            invoice.sale = sale
            invoice.type = sale.type_sale
            invoice.save()
        else:
            return Response(data={"fallo al finalizar, quedan pagos pendientes"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


class SaleListView(APIView, SerializingSupportMixin):
    permission_classes = []
    request_serializer = SaleSerializer

    def get(self, request: Request):
        sales = Sale.objects.filter(is_active=True)
        serializer = SaleSerializer(sales, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
