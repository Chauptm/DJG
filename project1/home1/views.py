from django.shortcuts import render
from django.views.generic.base import View
from .models import Product
from .serializers import ProductSerializers, UserSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import viewsets
from django.contrib.auth.models import User
from home1.permission import IsOwnerOrReadOnly
from rest_framework import permissions
# Create your views here.
class UserViewsets(viewsets.ReadOnlyModelViewSet):
    serializer_class= UserSerializers
    queryset= User.objects.all()
class ProductListDetail(viewsets.ModelViewSet):
    serializer_class= ProductSerializers
    queryset= Product.objects.all()

    authentication_classes=[SessionAuthentication, BasicAuthentication]
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    # lookup_field='id'
    # def get(self, request, id=None):
    #     if id:
    #         return self.retrieve(request)
    #     else:
    #         return self.list(request)
    # def post(self, request):
    #     return self.create(request)

    # def put(self, request, id=None):
    #     return self.update(request, id)
    # def delete(self, request,id):
    #     return self.destroy(request, id)

    # def get(self, request, format=None):
    #     product= Product.objects.all()
    #     serializer= ProductSerializers(product, many= True)
    #     return Response(serializer.data)

    # def post(self,request, format=None):
    #     serializer= ProductSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


