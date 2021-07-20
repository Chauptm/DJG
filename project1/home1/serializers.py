from django.db.models import fields
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    snippets= serializers.PrimaryKeyRelatedField(many=True, read_only= True)
    # owner= serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model =User
        fields=['id','username', 'snippets']

class ProductSerializers(serializers.ModelSerializer):
    def validate_name(self, value):
        if value.find('chau_')!=0:
        	raise serializers.ValidationError("No format!")
        return value

    owner= serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model= Product
        fields=['id','owner', 'name','status']

    # def create(self, validated_data):
    #     return super().create(**validated_data)    
    
    # def update(self, instance, validated_data):
    #     return super().update(instance, **validated_data)
