#rest_framework is what we installed in requirements : djangorestframework
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApi(APIView):
    #test APIView
    def get(self,request,format=None):
        """return a list of APIview features"""
        an_apiview = [
            'Uses Http methods as func (get,post,patch,put,delete)',
            'gives you control over app logic',
            'it is mapped manually to URLs',
        ]

        #it has to return a response obj. could be list or dict
        return Response({'msg':'hello','an_apiview':an_apiview})