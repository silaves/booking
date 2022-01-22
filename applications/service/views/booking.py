from django import forms

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from applications.service.models.booking import Booking
from applications.service.models.room import Room
from applications.service.models.sale import Sale
from .support import *


class BookingSerializer(serializers.ModelSerializer):
    type_sale = serializers.ChoiceField(required=True, choices=Sale.TYPE_SALE)

    class Meta:
        model = Booking
        fields = ['room', 'client', 'user', 'date_booking', 'date_entry', 'date_exit',
                  'number_days', 'type_sale']

    def create(self, validated_data):
        try:
            data = validated_data.pop('type_sale')
        except:
            pass
        return Booking.objects.create(**validated_data)

    def validate_room(self, value):
        if value.status != Room.AVAILABLE or value.is_active is False:
            raise forms.ValidationError('La habitacion no esta disponible')
        return value

    def validate_client(self, value):
        if value.is_active is False:
            raise forms.ValidationError('El cliente no esta activo')
        return value


class BookingUpdateSerializer(serializers.ModelSerializer):
    type_sale = serializers.ChoiceField(required=True, choices=Sale.TYPE_SALE)

    class Meta:
        model = Booking
        fields = ['client', 'user', 'date_entry', 'date_exit', 'number_days', 'status', 'type_sale']

    def validate_client(self, value):
        if value.is_active is False:
            raise forms.ValidationError('El cliente no esta activo')
        return value


class BookingView(APIView, SerializingSupportMixin):
    permission_classes = []
    request_serializer = BookingSerializer

    def post(self, request: Request):
        obj = BookingSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        booking = obj.save()
        sale = Sale()
        sale.status = Sale.IN_PROGRESS
        sale.total = booking.room.price_by_day*request.data.get('number_days')
        sale.type_sale = request.data['type_sale']
        sale.save()
        booking.sale = sale
        booking.status = Booking.PENDING
        booking.save()
        booking.room.status = Room.BOOKED
        booking.room.save()

        return Response(status=status.HTTP_200_OK)

    def put(self, request: Request, pk):
        try:
            booking = Booking.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        obj = BookingUpdateSerializer(booking, data=request.data, partial=True)
        obj.is_valid(raise_exception=True)
        obj.save()
        sale = booking.sale
        if request.data.get('number_days') is not None:
            sale.total = booking.room.price_by_day*request.data.get('number_days')
        if request.data.get('type_sale') is not None:
            sale.type_sale = request.data['type_sale']
        sale.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request: Request):
        bookings = Booking.objects.filter(is_active=True)
        serializer = BookingSerializer(bookings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int):
        try:
            booking = Booking.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        booking.is_active = False
        booking.room.status = Room.AVAILABLE
        booking.save()
        booking.sale.status = Sale.CANCELED
        booking.is_active = False
        booking.save()
        if Invoice.objects.filter(sale=booking.sale).exists():
            invoice = Invoice.objects.get(sale=booking.sale)
            invoice.is_active = False
            invoice.save()
        return Response(status=status.HTTP_200_OK)
