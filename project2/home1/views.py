from django.shortcuts import render

# Create your views here.

from .serializers import PersonSerialiers
from .models import Person
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
class ProductViewset(viewsets.ModelViewSet):
    queryset= Person.objects.all()
    serializer_class= PersonSerialiers
    authentication_classes=[JWTAuthentication]
    permission_classes= [IsAuthenticated]
    



