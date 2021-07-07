from django.http import request
from django.shortcuts import render
from django.views.generic.base import View
from .models import Product
from .serializers import ProductSerializers, UserSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import viewsets
from django.contrib.auth.models import User
from home1.permission import IsOwnerOrReadOnly
from home1.filters import ProductFilter
from home1.pagination import PaginationSet
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

# Create your views here.
class UserViewsets(viewsets.ReadOnlyModelViewSet):
    serializer_class= UserSerializers
    queryset= User.objects.all()

class ProductListDetail(viewsets.ModelViewSet):
    serializer_class= ProductSerializers
    # queryset = Product.objects.all()
    def get_queryset(self):
        user= self.request.user
        return Product.objects.filter(owner= user)
    filter_backends=[DjangoFilterBackend]
    filterset_class= (ProductFilter)
    # filterset_fields = ['name']
    pagination_class=PaginationSet
    authentication_classes=[SessionAuthentication]
    # authentication_classes=[TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    # pagination_class=[PageNumber]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)