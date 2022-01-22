from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.service.models.payment_method import PaymentMethod
from .support import *


class PaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ['number_document', 'type_method']


class PaymentMethodView(APIView, SerializingSupportMixin):
    permission_classes = []
    request_serializer = PaymentMethodSerializer

    def post(self, request: Request):
        obj = PaymentMethodSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(status=status.HTTP_200_OK)

    def put(self, request: Request, pk):
        try:
            payment_method = PaymentMethod.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        obj = PaymentMethodSerializer(payment_method, data=request.data, partial=True)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request: Request):
        payment_methods = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(payment_methods, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int):
        try:
            payment_method = PaymentMethod.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        payment_method.delete()
        return Response(status=status.HTTP_200_OK)
