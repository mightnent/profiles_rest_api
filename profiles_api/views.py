from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
# from rest_framework import filters
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers



class HelloApi(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self,request,pk=None):
        """update entire object"""
        #pk is primary key
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """partial update of object"""
        return Response({'method':'patch'})

    def delete(self, request,pk=None):
        """delete obj"""
        return Response({'method':'delete'})