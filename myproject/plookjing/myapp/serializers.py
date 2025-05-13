from rest_framework import serializers
from .models import Tree

class TreeSerializer(serializers.ModelSerializer):
    image_url = serializers.URLField(required=False, allow_null=True)

    class Meta:
        model = Tree
        fields = ['id', 'name', 'species', 'location', 'price', 'description', 'image_url']
