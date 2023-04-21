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
