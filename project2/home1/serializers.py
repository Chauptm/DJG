from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Person
class PersonSerialiers(serializers.ModelSerializer):
    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('khong du tuoi')
        return age
    class Meta:
        model= Person
        fields= '__all__'