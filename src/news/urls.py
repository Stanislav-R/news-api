from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import PostsViewSet, CommentsViewSet, UpvoteView

router = routers.DefaultRouter()
router.register("posts", PostsViewSet)
router.register("comments", CommentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:pk>/upvote/", UpvoteView.as_view()),
]
