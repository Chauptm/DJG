from django.db.models import fields
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class UserSerializers(serializers.HyperlinkedModelSerializer):
    snippets= serializers.HyperlinkedRelatedField(many=True,view_name='product-detail', read_only= True)
    # owner= serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model =User
        fields=['url','id','username', 'snippets']

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    def validate_name(self, value):
        if value.find('chau_')!=0:
        	raise serializers.ValidationError("Không theo định dạng")
        return value

    owner= serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model= Product
        fields=['url','id','owner', 'name','status']

    # def create(self, validated_data):
    #     return super().create(**validated_data)    
    
    # def update(self, instance, validated_data):
    #     return super().update(instance, **validated_data)
