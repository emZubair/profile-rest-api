from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Django API View testing """

    def get(self, request, format=None):
        """ Http get request """

        description = [
            'Api View uses HTTP methods as functions (GET, POST, DELETE, PUT & DELETE',
            'It inherits from Djagno Views',
            'You need to map it using a URL same like we do for Django Views'
        ]

        response = Response({'message': 'Hello', 'description': description})
        import pdb
        pdb.set_trace()
        return response
