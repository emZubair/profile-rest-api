from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from profile_api.serializers import HelloSerializers


class HelloApiView(APIView):
    """ Django API View testing """

    serializer_class = HelloSerializers

    def get(self, request, format=None):
        """ Http get request """

        description = [
            'Api View uses HTTP methods as functions (GET, POST, DELETE, PUT & DELETE',
            'It inherits from Djagno Views',
            'You need to map it using a URL same like we do for Django Views'
        ]

        return Response({'message': 'Hello', 'description': description})

    def post(self, request):
        """ Create Hello message with given name """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handle updating objects, will replace the fields that are not supplied """

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Update given fields & ignore missing fields """

        return Response({'patch': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete given object """

        return Response({'method': 'DELETE'})


class HelloViewsets(viewsets.ViewSet):
    """ Test API Viewsets """

    serializer_class = HelloSerializers

    def list(self, request):
        """ list viewset testing """

        description = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Router',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello Viewsets', 'description': description})

    def create(self, request):
        """ Create a new Hello message """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello: {name}'
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handle getting an object by its ID """

        return Response({'https_methods': 'GET', 'pk': pk})

    def update(self, request, pk=None):
        """ Handle updating an object """

        return Response({'http_methods': 'PUT', 'pk': pk})

    def partial_update(self, request, pk=None):
        """ Hanlde partially updating the object """

        return Response({'http_methods': 'PATCH', 'pk': pk})

    def destroy(self, request, pk):
        """ Handle deleting an object """

        return Response({'http_methos': 'DELETE', 'pk': pk})
