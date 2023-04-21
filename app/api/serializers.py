from rest_framework import serializers
from instagram.models import Posts


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'user', 'description', 'img', 'likes', 'comments', 'created_at')
        read_only_fields = ('id', 'created_at')
