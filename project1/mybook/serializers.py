from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Author, Book, Store, Publisher

class AuthorSerializer(serializers.ModelSerializer):
    # books_count= serializers.IntegerField()
    class Meta:
        model= Author
        fields= '__all__'

class AuthorReadOnlySerializer(serializers.Serializer):
    name= serializers.CharField()

class AuthorBookCount(serializers.Serializer):
    name= serializers.CharField(read_only= True)
    books_count= serializers.IntegerField(read_only= True)

class BookSerializer(serializers.ModelSerializer):
    authors= serializers.ListField(
        child = AuthorReadOnlySerializer(),
        source = 'authors.all'
    )
    publisher= serializers.ReadOnlyField(source='publisher.name')
    class Meta:
        model= Book
        fields= ['name', 'page', 'price','rating', 'authors', 'publisher', 'pubdate']
        # fields= '__all__'

class BookAuthorCount(serializers.Serializer):
    name= serializers.CharField(read_only= True)
    author_count= serializers.IntegerField(read_only= True)


class BoolReadOnlySerializer(serializers.Serializer):
    name= serializers.CharField(read_only= True)
class StoreSerializer(serializers.ModelSerializer):
    books = serializers.ListField(
        child= BoolReadOnlySerializer(),
        source= 'books.all'
    )
    class Meta:
        model= Store
        # fields= '__all__'
        fields= ['name', 'books']

class PublisherSerializer(serializers.ModelSerializer):
    # pubs= Publisher.objects.annotate(Count(F()))

    class Meta:
        model= Publisher
        fields= '__all__'