from django.shortcuts import render

# Create your views here.


from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class TestAPIViewset(viewsets.ViewSet):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    permission_classes     = [IsAuthenticated]
    parser_classes         = (MultiPartParser,)

    # Create Project Api
    @action(methods=['GET' ], detail=False)
    def testapi(self,request):
        return Response({'message': 'middleware request success'})