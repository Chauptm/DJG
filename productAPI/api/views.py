import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

from .serializers import ProductSerializer
from .models import Product
from django.http import Http404

@api_view(['GET'])
def showAll(request):
    product= Product.objects.all()
    serializer= ProductSerializer(product, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewProduct(request, pk):
    try:
        product= Product.objects.get(id=pk)
        serializer= ProductSerializer(product, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
            raise Http404
    # product= Product.objects.get(id=pk)
    # serializer= ProductSerializer(product, many=False)
    # return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer= ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateProduct(request, pk):
    product= Product.objects.get(id=pk)
    serializer= ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteProduct(request, pk):
    product= Product.objects.get(id=pk)
    product.delete()
    return Response("Xoá thành công")