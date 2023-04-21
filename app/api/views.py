from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from instagram.models import Posts
from rest_framework.response import Response
from api.serializers import PostsSerializer


# Create your views here.


class PostsView(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        object = Posts.objects.filter(id=self.kwargs['pk']).first()
        serializer = PostsSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class PostDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        object = Posts.objects.filter(id=self.kwargs['pk']).first()
        object_id = {'delete post pk': object.id}
        object.delete()
        return Response(object_id, status=204)

class LikeUpdateView(APIView):
    def get(self, request, *args, **kwargs):
        object = Posts.objects.filter(id=self.kwargs['pk']).first()
        user = request.user
        if object in user.liked_posts.all():
            user.liked_posts.remove(Posts.objects.get(id=self.kwargs['pk']))
            object.likes -= 1
            object.save()
            user.save()
            post_liked = {'like': 'removed like'}
        else:
            user.liked_posts.add(Posts.objects.get(id=self.kwargs['pk']))
            object.likes += 1
            object.save()
            user.save()
            post_liked = {'like': 'put like'}
        return Response(post_liked, status=204)
