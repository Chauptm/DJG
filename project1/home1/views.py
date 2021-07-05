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
from home1.filters import IsOwnerFilterBackend
from home1.pagination import PaginationSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
class UserViewsets(viewsets.ReadOnlyModelViewSet):
    serializer_class= UserSerializers
    queryset= User.objects.all()
    # pagination_class=PaginationSetUser

class ProductListDetail(viewsets.ModelViewSet):
    serializer_class= ProductSerializers
    queryset = Product.objects.all()
    filter_backends=[DjangoFilterBackend, IsOwnerFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields= ['name']
    ordering_fields= ['name']
    pagination_class=PaginationSet
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    # authentication_classes=[TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    # pagination_class=[PageNumber]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)