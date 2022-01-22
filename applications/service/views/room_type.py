from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.service.models.room_type import RoomType
from .support import *


class RoomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomType
        fields = ['code', 'description']


class RoomTypeView(APIView, SerializingSupportMixin):
    permission_classes = []
    request_serializer = RoomTypeSerializer

    def post(self, request: Request):
        obj = RoomTypeSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int):
        try:
            room_type = RoomType.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        obj = RoomTypeSerializer(room_type, data=request.data, partial=True)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request: Request):
        room_types = RoomType.objects.all()
        serializer = RoomTypeSerializer(room_types, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int):
        try:
            room_type = RoomType.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        room_type.delete()
        return Response(status=status.HTTP_200_OK)
