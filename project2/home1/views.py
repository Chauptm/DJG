from django.shortcuts import render

# Create your views here.

from .serializers import PersonSerialiers
from .models import Person
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
class PersonViewset(viewsets.ModelViewSet):
    queryset= Person.objects.all()
    serializer_class= PersonSerialiers
    # authentication_classes=[BasicAuthentication]
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes= [IsAdminUser]
    # permission_classes= [AllowAny]
    # permission_classes= [IsAuthenticatedOrReadOnly]
    # permission_classes= [DjangoModelPermissions]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    



