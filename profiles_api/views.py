from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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

class HelloApiViewset(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return a hello msg"""
        a_viewset =[
            'use list,CRU(+partial_update)D',
            'auto map URLs using router',
            'provide more functionality with less code'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """create a new hello msg, i.e. like a post"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """sth like get"""
        return Response({'HTTP METHOD':'GET'}) 

    def update(self,request,pk=None):
        return Response({'HTTP METHOD':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'HTTP METHOD':'PATCH'})   
    
    def destroy(self,request,pk=None):
        return Response({'HTTP METHOD':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.UPM.all()
    #these var names are not anyhow assigned. they carry meaning
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields =('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES