from decimal import Decimal

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.service.models.payment import Payment
from applications.service.models.booking import Booking
from applications.service.models.sale import Sale
from .support import *


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['payment_amount', 'payment_method', 'sale']


class PaymentView(APIView, SerializingSupportMixin):
    permission_classes = []
    request_serializer = PaymentSerializer

    def post(self, request: Request, pk_booking: int):
        try:
            booking = Booking.objects.get(pk=pk_booking)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if is_paid(booking.sale):
            return Response(data={"se concluyo con el pago"}, status=status.HTTP_400_BAD_REQUEST)
        obj = PaymentSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        payment = obj.save()
        if is_paid(booking.sale):
            booking.status = Booking.PAID
            booking.save()
        return Response(status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int):
        try:
            payment = Payment.objects.get(pk=pk, is_active=True)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        obj = PaymentSerializer(payment, data=request.data, partial=True)
        obj.is_valid(raise_exception=True)
        obj.save()
        if is_paid(obj.sale):
            booking.status = Booking.PAID
            booking.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request: Request):
        payment = Payment.objects.filter(is_active=True)
        serializer = PaymentSerializer(payment, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int):
        try:
            payment = Payment.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        payment.is_active = False
        payment.save()
        return Response(status=status.HTTP_200_OK)


def is_paid(sale: Sale):
    payments = Payment.objects.filter(sale=sale, is_active=True)
    sum_total = Decimal(0.0)
    for pay in payments:
        sum_total += pay.payment_amount
    if sum_total >= sale.total:
        return True
    print(sum_total)
    return False
