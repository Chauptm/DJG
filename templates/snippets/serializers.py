from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    owner= serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = ['url','id', 'username', 'snippets', 'owner']

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    owner= serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight','owner', 'title', 'code', 'linenos', 'language', 'style']

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
