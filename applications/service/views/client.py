from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.service.models.client import Client
from .support import *


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['nit', 'name']


class ClientView(APIView, SerializingSupportMixin):
    permission_classes = []
    request_serializer = ClientSerializer

    def post(self, request: Request):
        obj = ClientSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int):
        try:
            client = Client.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        obj = ClientSerializer(client, data=request.data, partial=True)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request: Request):
        from django.conf import settings
        print(settings.MEDIA_ROOT)
        clients = Client.objects.filter(is_active=True)
        serializer = ClientSerializer(clients, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int):
        try:
            client = Client.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        client.is_active = False
        client.save()
        return Response(status=status.HTTP_200_OK)
