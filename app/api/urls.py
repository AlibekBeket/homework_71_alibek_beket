from django.urls import path, include
from rest_framework import routers
from api.views import PostsView

router = routers.DefaultRouter()
router.register('posts', PostsView)

urlpatterns = [
    path('', include(router.urls)),
]