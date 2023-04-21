from django.urls import path

from instagram.views.posts import PostsListView, PostAddView, LikePostView, PostDetailView, CommentAddView

urlpatterns = [
    path('', PostsListView.as_view()),
    path('posts/', PostsListView.as_view(), name='posts_list'),
    path('posts/add', PostAddView.as_view(), name='post_create'),
    path('posts/like/<int:pk>', LikePostView.as_view(), name='post_like'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/comment_add', CommentAddView.as_view(), name='comment_add'),
]
