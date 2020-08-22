from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=500, null=True)
    score = serializers.IntegerField(null=True)
    description = serializers.TextField()
    city = serializers.CharField(max_length=500, null=True)
    price = serializers.IntegerField(null=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('score', instance.code)
        instance.linenos = validated_data.get('description', instance.linenos)
        instance.language = validated_data.get('city', instance.language)
        instance.style = validated_data.get('price', instance.style)
        instance.save()
        return instance