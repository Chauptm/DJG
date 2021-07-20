from .pagination import PaginationSet
from django.db.models import Count, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .filters import PublisherFilter
from .models import Author, Book, Publisher, Store
from .serializers import (AuthorBookCount, AuthorSerializer, BookAuthorCount,
                          BookSerializer, PublisherSerializer, StoreSerializer)


class AuthorViewsets(viewsets.ModelViewSet):
    serializer_class= AuthorSerializer
    queryset= Author.objects.all()

    @action(
        detail=False,
        methods=['GET'],
        url_path='author_book_count',
        url_name='author_book_count'
    )
    def authors(self, request):
        authors_book_count= Author.objects.annotate(books_count= Count(F('book')))
        serializer = AuthorBookCount(authors_book_count, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



class BookViewsets(viewsets.ModelViewSet):
    serializer_class= BookSerializer
    queryset= Book.objects.all()

    @action(
        detail=False,
        methods=['GET'],
        url_path='book_author_count',
        url_name='book_author_count'
    )
    def books(self, request):
        bac= Book.objects.annotate(author_count=Count(F('authors')))
        serializer = BookAuthorCount(bac, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    pagination_class= (PaginationSet)
class StoreViewsets(viewsets.ModelViewSet):
    serializer_class= StoreSerializer   
    queryset= Store.objects.all()

class PublisherViewsets(viewsets.ModelViewSet):
    serializer_class= PublisherSerializer   
    queryset= Publisher.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_class= (PublisherFilter)



