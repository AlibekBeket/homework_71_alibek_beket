from django.urls import path, include
from rest_framework import routers
from api.views import PostsView, PostUpdateView, PostDeleteView, LikeUpdateView

router = routers.DefaultRouter()
router.register('posts', PostsView)

urlpatterns = [
    path('', include(router.urls)),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='api_post_update'),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name='api_post_delete'),
    path('post_like/<int:pk>/', LikeUpdateView.as_view(), name='api_post_like'),
]
