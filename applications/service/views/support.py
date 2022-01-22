from rest_framework import serializers


class SerializationException(Exception):
    pass


class SerializingSupportMixin:
    request_serializer: serializers.Serializer
    response_serializer: serializers.Serializer

    def deserialize_request(self, request):
        if not self.request_serializer:
            raise Exception("Request serializer cannot be None")
        serializer = self.request_serializer(data=request.data)
        if not serializer.is_valid():
            raise SerializationException(f"Incorrect format of request data {request.data}")
        return serializer.save()

    def deserialize_list_request(self, request):
        if not self.request_serializer:
            raise Exception("Request serializer cannot be None")
        serializer = self.request_serializer(data=request.data, many=True)
        if not serializer.is_valid():
            raise SerializationException(f"Incorrect format of request data {request.data}")
        return serializer.save()

    def serialize_response_data(self, response_instance):
        if not self.response_serializer:
            raise Exception("Response serializer cannot be None")
        resp_serializer_instance = self.response_serializer(response_instance)
        return resp_serializer_instance.data
