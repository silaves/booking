from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.service.models.room import Room
from .support import *


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['code', 'location', 'description', 'feature', 'price_by_day', 'status', 'room_type']


class RoomView(APIView, SerializingSupportMixin):
    permission_classes = []
    request_serializer = RoomSerializer

    def post(self, request: Request):
        obj = RoomSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int):
        try:
            room = Room.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        obj = RoomSerializer(room, data=request.data, partial=True)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request: Request):
        rooms = Room.objects.filter(status=Room.AVAILABLE, is_active=True)
        serializer = RoomSerializer(rooms, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int):
        try:
            room = Room.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        room.is_active = False
        room.save()
        return Response(status=status.HTTP_200_OK)
