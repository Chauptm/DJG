from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http.response import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, generics, status, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView

from home1.filters import ProductFilter, UserFilter
from home1.pagination import PaginationSet
from home1.permission import IsOwnerOrReadOnly

from .models import Product
from .serializers import ProductSerializers, UserSerializers


class Auth(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response(
                {
                    'username, password': ['This fields are required.']
                },
                status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {
                    'detail': ['Invalid Credentials']
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key,
                'user_id': user.pk, 
                'email': user.email
            },
            status=status.HTTP_200_OK
        )
class UserViewsets(viewsets.ModelViewSet):
    serializer_class= UserSerializers
    queryset= User.objects.all()

    # @action(detail=True, methods=['POST'])


class ProductListDetail(viewsets.ModelViewSet):
    serializer_class= ProductSerializers
    queryset = Product.objects.all()
    def get_queryset(self):
        # print("hello")
        user= self.request.user
        self.request.data
        return Product.objects.filter(owner= user)
    filter_backends=[DjangoFilterBackend]
    filterset_class= (ProductFilter)
    # filterset_fields = ['name']
    pagination_class=PaginationSet
    authentication_classes=[SessionAuthentication,TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
