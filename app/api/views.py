from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from instagram.models import Posts

from api.serializers import PostsSerializer


# Create your views here.


class PostsView(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
